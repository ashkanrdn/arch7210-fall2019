import math
from turtle import TNavigator, Vec2D
from ScaledTurtle import ScaledTurtle
from MotionVector import MotionVector


# https://introcs.cs.princeton.edu/python/34nbody/

# Gravitational constant in cubic meters per kilogram per seconds squared (m3⋅kg−1⋅s−2)
G = 6.674e-11

class CelestialTurtle(ScaledTurtle):

    # Mass of the turtle in kilograms
    mass = 0.0

    # Speed of the turtle in meters per second
    _objectSpeed = 0.0

    def __init__(self, mass=0.0, velocity=MotionVector(0, 0)):
        super().__init__(shape='circle')
        super().speed(0)
        self.radians()
        self.penup()
        self.mass = mass
        self.setvelocity(velocity)

    def velocity(self):
        return MotionVector(self._objectSpeed, self.heading())
    
    def setvelocity(self, velocity):
        v = MotionVector(velocity)
        self._objectSpeed = v.speed()

        heading = v.heading()
        if heading is not None:
            self.setheading(heading)

    # Moves the turtle by applying the given force (a MotionVector) for the given number of seconds.
    # Adapted from https://introcs.cs.princeton.edu/python/34nbody/body.py.html
    def move(self, force, time):
        acceleration = force * (1 / self.mass)
        velocity = MotionVector(self.velocity() + (acceleration * time))
        position = self.position() + (velocity * time)
        self.setposition(position)
        self.setvelocity(velocity)

    # Calculates the force exerted on this turtle by another CelestialTurtle
    # Adapted from https://introcs.cs.princeton.edu/python/34nbody/body.py.html
    def forceFrom(self, other):
        delta = MotionVector(other.pos() - self.pos())
        distance = abs(delta)
        magnitude = G * self.mass * other.mass / distance / distance
        return MotionVector(magnitude, delta.heading())
        
    

    