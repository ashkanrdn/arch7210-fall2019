import unittest

from turtle import Screen, Turtle, Vec2D
from ScaledTurtle import ScaledTurtle

class ScaledTurtleTest(unittest.TestCase):

    def _setup(self, pixelPosition=Vec2D(0, 0), pixelsPerUnit=1.0, heading=0):
        t = ScaledTurtle()
        t.hideturtle()
        t.setheading(heading)
        t._scaleFactor = pixelsPerUnit
        Turtle.setpos(t, pixelPosition)
        return t

    def test_pixelsPerUnit(self):
        t = self._setup(pixelsPerUnit=10)
        self.assertEqual(t.pixelsPerUnit(), 10)

    def test_unitsPerPixel(self):
        t = self._setup(pixelsPerUnit=10)
        self.assertEqual(t.unitsPerPixel(), 0.1)
    
    def test_setPixelsPerUnit(self):
        t = self._setup()
        t.setPixelsPerUnit(10)
        self.assertEqual(t._scaleFactor, 10)

    def test_setUnitsPerPixel(self):
        t = self._setup()
        t.setUnitsPerPixel(10)
        self.assertEqual(t._scaleFactor, 0.1)

    def test_pos(self):
        t = self._setup(pixelsPerUnit=10, pixelPosition=(120, 240))
        pos = t.pos()
        self.assertEqual(pos[0], 12)
        self.assertEqual(pos[1], 24)

    def test_xcor(self):
        t = self._setup(pixelsPerUnit=10, pixelPosition=(120, 240))
        self.assertEqual(t.xcor(), 12)

    def test_ycor(self):
        t = self._setup(pixelsPerUnit=10, pixelPosition=(120, 240))
        self.assertEqual(t.ycor(), 24)

    def test_setx(self):
        t = self._setup(pixelsPerUnit=10)
        t.setx(12)
        self.assertEqual(Turtle.xcor(t), 120)

    def test_sety(self):
        t = self._setup(pixelsPerUnit=10)
        t.sety(24)
        self.assertEqual(Turtle.xcor(t), 240)

    def test_goto(self):
        t = self._setup(pixelsPerUnit=10)
        t.goto(12, 24)
        pos = Turtle.pos(t)
        self.assertEqual(pos[0], 120)
        self.assertEqual(pos[1], 240)

    def test_forward(self):
        t = self._setup(pixelsPerUnit=10)
        t.forward(12)
        self.assertEqual(Turtle.xcor(t), 120)

    def test_back(self):
        t = self._setup(pixelsPerUnit=10)
        t.back(12)
        self.assertEqual(Turtle.xcor(t), -120)

    def test_distance(self):
        t1 = self._setup(pixelsPerUnit=10, pixelPosition=(0, 0))
        self.assertEqual(t1.distance(30, 40), 50)

        t2 = self._setup(pixelsPerUnit=10, pixelPosition=(300, 400))
        self.assertEqual(t1.distance(t2), 50)


if __name__ == '__main__':
    Screen().tracer(0, 0) # Don't waste time drawing
    unittest.main()