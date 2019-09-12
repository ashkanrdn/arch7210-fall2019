from astropy import units
from astropy.coordinates import CartesianRepresentation
from CelestialTurtle import CelestialTurtle

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
