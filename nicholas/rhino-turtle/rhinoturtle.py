import rhinoscriptsyntax as rs
from Rhino.RhinoMath import ToRadians
from Rhino.Geometry import Plane, Point3d, Vector3d
from System.Drawing import Color

class Turtle(object):

    def __init__(self):
        self._pose = Plane.WorldXY
        self._penDown = True
        self.color = Color.FromArgb(0)
        self.width = 0

    @property
    def position(self):
        return self._pose.Origin

    @position.setter
    def position(self, newPosition):
        if self._penDown:
            self._drawLine(newPosition)
        self._pose.Origin = newPosition

    @property
    def heading(self):
        return self._pose.XAxis

    @heading.setter
    def heading(self, newHeading):
        vector = Vector3d(newHeading)
        vector.Unitize()
        self._pose.XAxis = vector

    def forward(self, distance):
        self.move(self.heading * distance)

    def back(self, distance):
        self.forward(-distance)

    def left(self, angle):
        self._pose.Rotate(ToRadians(angle), self._pose.ZAxis)

    def right(self, angle):
        self.left(-angle)

    def down(self, angle):
        self._pose.Rotate(ToRadians(angle), self._pose.YAxis)

    def up(self, angle):
        self.down(-angle)

    def rollLeft(self, angle):
        self._pose.Rotate(ToRadians(angle), self._pose.XAxis)

    def rollRight(self, angle):
        self.left(-angle)

    @property
    def x(self):
        """The turtle's x coordinate."""
        return self._pose.OriginX

    @x.setter
    def x(self, x):
        self.position = Point3d(x, self._pose.OriginY, self._pose.OriginZ)

    @property
    def y(self):
        """The turtle's y coordinate."""
        return self._pose.OriginY

    @y.setter
    def y(self, y):
        self.position = Point3d(self._pose.OriginX, y, self._pose.OriginZ)

    @property
    def z(self):
        """The turtle's z coordinate."""
        return self._pose.OriginZ

    @z.setter
    def setz(self, z):
        self.position = Point3d(self._pose.OriginX, self._pose.OriginY, z)

    def goto(self, x=None, y=None, z=None):
        self.position = Point3d(x or self.X, y or self.Y, z or self.Z)

    def move(self, vector):
        if self._penDown:
            self._drawLine(self._pose.Origin + vector)
        self._pose.Translate(vector)

    def _drawLine(self, newPosition):
        line = rs.AddLine(self._pose.Origin, newPosition)
        rs.ObjectColor(line, self.color)
        rs.ObjectPrintColor(line, self.color)
        rs.ObjectPrintWidth(line, self.width)

    def penUp(self):
        self._penDown = False

    def penDown(self):
        self._penDown = True


# Clear the board
rs.DeleteObjects(rs.AllObjects(select=True))

red = Color.FromArgb(255, 0, 0)
green = Color.FromArgb(0, 255, 0)
blue = Color.FromArgb(0, 0, 255)

t = Turtle()
t.penUp()
t.X = -5
t.Y = -5
t.Z = -5
t.penDown()

t.color = red
t.forward(10)
t.up(90)

t.width = 1
t.color = blue
t.forward(10)
t.left(90)

t.width = 2
t.color = green
t.forward(10)
t.up(90)

t.width = 3
t.color = red
t.forward(10)
t.left(90)

t.width = 4
t.color = blue
t.forward(10)
t.up(90)

t.width = 5
t.color = green
t.forward(10)
t.left(90)
