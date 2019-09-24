import json
from Rhino.Display import DisplayConduit
from Rhino.Geometry import Point3d, Vector3d
from System.Drawing import Color
import rhinoscriptsyntax as rs
import rhinoturtle

# Gravitational constant in cubic AU per kilogram per days squared
G = 1.488e-34

class Body(rhinoturtle.Turtle):
    """A celestial body such as a moon, planet, or star.
    Adapted from https://introcs.cs.princeton.edu/python/34nbody/body.py.html"""

    def __init__(self, name='', mass=0.0, radius=0):
        rhinoturtle.Turtle.__init__(self)
        self.penup()
        self.name = name
        self.mass = mass  # The mass of the turtle in kilograms.
        self.speed = 0    # Speed of the turtle in AU per day.
        self.radius = radius # Radius of the turtle in kilometers.

    @property
    def velocity(self):
        """The velocity of the body."""
        return self.heading * self.speed

    @velocity.setter
    def velocity(self, velocity):
        self.speed = velocity.Length
        self.heading = velocity

    def move(self, force, time):
        """Move the body by applying the `force` for an amount of `time`."""
        acceleration = force / self.mass
        self.velocity = self.velocity + (acceleration * time)
        self.position = self.position + (self.velocity * time)

    def forceFrom(self, other):
        """Calculate the force exerted on this body by another celestial body."""
        delta = other.position - self.position
        distance = delta.Length
        magnitude = G * self.mass * other.mass / distance / distance
        delta.Unitize()
        return delta * magnitude

    def done(self):
        self._conduit.Enabled = False



class System(object):
    """A collection of gravitationally bound celestial bodies."""

    def __init__(self, center):
        self.bodies = []
        self.center = center

    def add(self, celestialTurtle):
        """Add a new celestial body to the system."""
        self.bodies.append(celestialTurtle)

    def advance(self, time):
        """Advance the system by the given amount of time."""
        for targetBody in self.bodies:
            force = None
            for otherBody in self.bodies:
                if otherBody != targetBody:
                    if force is None:
                        force = targetBody.forceFrom(otherBody)
                    else:
                        force += targetBody.forceFrom(otherBody)
            targetBody.move(force, time)

    @classmethod
    def fromJSON(cls, filePath):
        with open(filePath, 'r') as file:
            parsed = json.load(file)
            system = cls(Point3d(0, 0, 0))

            for data in parsed['bodies']:
                body = Body(data['name'], data['mass'], data['radius'])
                body.position = Point3d(*data['position'])
                body.velocity = Vector3d(*data['velocity'])
                body.color = Color.FromArgb(*data['color'])
                body.pendown()
                system.add(body)

            return system
