import math
import re
from astropy import units
from astropy.coordinates import CartesianRepresentation, PhysicsSphericalRepresentation
from astropy.time import Time
from astroquery.jplhorizons import Horizons
from ScaledTurtle import ScaledTurtle

# Gravitational constant in cubic meters per kilogram per seconds squared (m3⋅kg−1⋅s−2)
G = 6.674e-11 * units.meter**3 / units.kilogram / units.second**2

# A CelestialTurtle represents a celestial body such as a moon, planet, or star.
class CelestialTurtle(ScaledTurtle):

    # The mass of the turtle
    mass = 0 * units.kilogram

    # The position of the turtle in 3D space
    _position3D = CartesianRepresentation(0, 0, 0)

    # The velocity of the turtle in 3D space
    _velocity3D = CartesianRepresentation(0, 0, 0)

    def __init__(self, mass=0.0):
        super().__init__(shape='circle')
        self.turtlesize(0.1, 0.1, 10)
        self.radians()
        self.penup()
        self.mass = mass

    def velocity(self):
        return self._velocity3D
    
    def setvelocity(self, velocity):
        if not isinstance(velocity, CartesianRepresentation):
            velocity = CartesianRepresentation(velocity)
        self._velocity3D = velocity
        self.setheading(math.atan2(velocity.y.value, velocity.x.value))
    
    def goto(self, x, y=None):
        if isinstance(x, CartesianRepresentation):
            self._position3D = x
            x_km = self._position3D.x.to(units.kilometer).value
            y_km = self._position3D.y.to(units.kilometer).value
            super().goto(x_km, y_km)
        else:
            super().goto(x, y)
            x_km = super().xcor() * units.kilometer
            y_km = super().ycor() * units.kilometer
            self._position3D = CartesianRepresentation(x_km, y_km, self._position3D.z)

    setposition = goto
    setpos = goto

    # Moves the turtle by applying the given force for the given amount of time.
    # Adapted from https://introcs.cs.princeton.edu/python/34nbody/body.py.html
    def move(self, force, time):
        acceleration = force / self.mass
        velocity = self._velocity3D + (acceleration * time)
        position = self._position3D + (velocity * time)
        self.setposition(position)
        self.setvelocity(velocity)

    # Calculates the force exerted on this turtle by another CelestialTurtle
    # Adapted from https://introcs.cs.princeton.edu/python/34nbody/body.py.html
    def forceFrom(self, other):
        delta = other._position3D - self._position3D
        direction = PhysicsSphericalRepresentation.from_cartesian(delta)
        distance = direction.r
        magnitude = G * self.mass * other.mass / distance / distance
        force = PhysicsSphericalRepresentation(direction.phi, direction.theta, magnitude)
        return force.to_cartesian()


# A system is a collection of gravitationally-bound turtles.
class System:

    bodies = []

    def __init__(self, center, scale, startTime=Time.now()):
        self.center = center
        self.scale = scale
        self.startTime = startTime

    # Looks up a solar system body and adds it to the system.
    def lookup(self, id, type, mass=0*units.kilogram):
        data = Lookup(id, type, self.center, self.startTime)
        body = CelestialTurtle(data.mass())
        self.add(body)
        body.setposition(data.position())
        body.setvelocity(data.velocity())
        return body

    # Adds a new turtle to the system.
    def add(self, celestialTurtle):
        celestialTurtle.setUnitsPerPixel(self.scale)
        self.bodies.append(celestialTurtle)

    # Advances the system by the given amount of time.
    def advance(self, time):
        for targetBody in self.bodies:
            force = None
            for otherBody in self.bodies:
                if otherBody != targetBody:
                    if force is None:
                        force = targetBody.forceFrom(otherBody)
                    else:
                        force += targetBody.forceFrom(otherBody)
            targetBody.move(force, time)


_massPattern = re.compile('Mass,?\s*x?10\^([0-9]+)\s*\(?kg\)?\s*=\s*~?([.0-9]+)')

# Retrieves information about a solar system object from JPL's Horizons service.
class Lookup:

    vectors = None
    elements = None

    def __init__(self, id, idType, relativeTo, time=Time.now()):
        self.obj = Horizons(id=id, id_type=idType, location=relativeTo, epochs=time.jd)

    def mass(self):
        if self.elements is None:
            self.elements = self.obj.elements(get_raw_response=True)

        match = _massPattern.search(self.elements)
        if match:
            n, m = match.group(1), match.group(2)
            kg = float(f'{m}e{n}')
            return kg * units.kilogram
        return None

    def vectorData(self, columnName):
        if self.vectors is None:
            self.vectors = self.obj.vectors()
        return self.vectors[columnName].quantity[0]
    
    def position(self):
        return CartesianRepresentation(self.vectorData('x'), self.vectorData('y'), self.vectorData('z'))

    def velocity(self):
        return CartesianRepresentation(self.vectorData('vx'), self.vectorData('vy'), self.vectorData('vz'))
    
    def assignTo(self, celestialTurtle):
        celestialTurtle.mass = self.mass()
        celestialTurtle.setposition(self.position())
        celestialTurtle.setvelocity(self.velocity())
