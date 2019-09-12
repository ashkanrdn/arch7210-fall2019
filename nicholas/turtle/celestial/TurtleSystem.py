from CelestialTurtle import CelestialTurtle
from MotionVector import MotionVector

class TurtleSystem:

    bodies = []

    def __init__(self, scale):
        self.scale = scale

    # Adds a new body to the system.
    def addBody(self, mass, velocity=(0,0)):
        t = CelestialTurtle(mass, velocity)
        t.setUnitsPerPixel(self.scale)
        self.bodies.append(t)
        return t

    # Advances the system by time seconds.
    def advance(self, time):
        for targetBody in self.bodies:
            force = MotionVector(0, 0)
            for otherBody in self.bodies:
                if otherBody != targetBody:
                    force += targetBody.forceFrom(otherBody)
            targetBody.move(force, time)
