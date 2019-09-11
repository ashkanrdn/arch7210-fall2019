import math
import turtle
import unittest

from MotionVector import MotionVector

class MotionVectorTest(unittest.TestCase):

    def test_new(self):
        sqrt2 = math.sqrt(2)
        cases = [
            (0, 0, 0, 0),
            (0, 1, 0, 0),
            (0, -1, 0, 0),

            (1, 0, 1, 0),
            (1, math.pi / 2, 0, 1),
            (1, math.pi, -1, 0),
            (1, 3 * math.pi / 2, 0, -1),
            
            (sqrt2, math.pi / 4, 1, 1),
            (sqrt2, 3 * math.pi / 4, -1, 1),
            (sqrt2, 5 * math.pi / 4, -1, -1),
            (sqrt2, 7 * math.pi / 4, 1, -1)
        ]

        for speed, heading, x, y in cases:
            v = MotionVector(MotionVector(speed, heading))
            self.assertAlmostEqual(v[0], x, msg=f'X component of MotionVector({speed}, {heading})')
            self.assertAlmostEqual(v[1], y, msg=f'Y component of MotionVector({speed}, {heading})')

    def test_heading(self):
        cases = [
            (0, 0, None),
            (0, 1, math.pi / 2),
            (0, -1, -math.pi / 2),

            (1, 0, 0),
            (1, 1, math.pi / 4),
            (1, -1, -math.pi / 4),

            (-1, 0, math.pi),
            (-1, 1, 3 * math.pi / 4),
            (-1, -1, -3 * math.pi / 4)
        ]

        for x, y, expected in cases:
            v = MotionVector(turtle.Vec2D(x, y))
            self.assertAlmostEqual(v.heading(), expected, msg=f'Vec2D({x}, {y})')

    def test_speed(self):
        sqrt2 = math.sqrt(2)
        cases = [
            (0, 0, 0),
            (0, 1, 1),
            (0, -1, 1),

            (1, 0, 1),
            (1, 1, sqrt2),
            (1, -1, sqrt2),

            (-1, 0, 1),
            (-1, 1, sqrt2),
            (-1, -1, sqrt2)
        ]

        for x, y, expected in cases:
            v = MotionVector(turtle.Vec2D(x, y))
            self.assertAlmostEqual(v.speed(), expected, msg=f'Vec2D({x}, {y})')


if __name__ == '__main__':
    unittest.main()