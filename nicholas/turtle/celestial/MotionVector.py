import math
from turtle import Vec2D

# Extends turtle's Vec2D class with methods for getting the magitude and heading.
class MotionVector(Vec2D):

    def __new__(cls, speed, heading=None):
        if heading is None:
            return Vec2D.__new__(cls, speed[0], speed[1])
        else:
            x = speed * math.cos(heading)
            y = speed * math.sin(heading)
            return Vec2D.__new__(cls, x, y)

    # Returns the vector's heading in radians.
    def heading(self):
        if self[0] == 0 and self[1] == 0:
            return None
        return math.atan2(self[1], self[0])

    # Returns the vector's magnitude.
    def speed(self):
        return math.sqrt(self[0]**2 + self[1]**2)
