import math
from ScaledTurtle import ScaledTurtle

from astropy.coordinates import CartesianRepresentation, PhysicsSphericalRepresentation
from astropy import units

# Gravitational constant in cubic meters per kilogram per seconds squared (m3⋅kg−1⋅s−2)
G = 6.674e-11 * units.meter**3 / units.kilogram / units.second**2

class CelestialTurtle(ScaledTurtle):

    # The mass of the turtle
    mass = 0 * units.kilogram

    # The position of the turtle in 3D space
    _position3D = CartesianRepresentation(0, 0, 0)

    # The velocity of the turtle in 3D space
    _velocity3D = CartesianRepresentation(0, 0, 0)

    def __init__(self, mass=0.0, velocity=CartesianRepresentation(0, 0, 0)):
        super().__init__(shape='circle')
        self.turtlesize(0.1, 0.1, 10)
        self.radians()
        self.penup()
        self.mass = mass
        self.setvelocity(velocity)

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
