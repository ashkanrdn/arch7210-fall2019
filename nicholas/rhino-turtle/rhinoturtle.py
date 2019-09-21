import rhinoscriptsyntax as rs
from Rhino.RhinoMath import ToRadians
from Rhino.Geometry import Plane, Point3d, Vector3d
from System.Drawing import Color

class Turtle:

    def __init__(self):
        self._pose = Plane.WorldXY
        self._penDown = True
        self.color = Color.FromArgb(0)
        self.width = 0

    def position(self):
        return self._pose.Origin

    def heading(self):
        return self._pose.XAxis

    def forward(self, distance):
        self.move(self.heading() * distance)

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

    def setPosition(self, x, y=0, z=0):
        if isinstance(x, Point3d):
            self.moveTo(x)
        else:
            self.moveTo(Point3d(x, y, z))

    def setX(self, x):
        self.moveTo(Point3d(x, self._pose.OriginY, self._pose.OriginZ))

    def setY(self, y):
        self.moveTo(Point3d(self._pose.OriginX, y, self._pose.OriginZ))

    def setZ(self, z):
        self.moveTo(Point3d(self._pose.OriginX, self._pose.OriginY, z))

    def move(self, vector):
        if self._penDown:
            newPosition = self._pose.Origin + vector
            line = rs.AddLine(self._pose.Origin, newPosition)
            rs.ObjectColor(line, self.color)
            rs.ObjectPrintColor(line, self.color)
            rs.ObjectPrintWidth(line, self.width)
        self._pose.Translate(vector)

    def moveTo(self, newPosition):
        if self._penDown:
            line = rs.AddLine(self._pose.Origin, newPosition)
            rs.ObjectColor(line, self.color)
            rs.ObjectPrintColor(line, self.color)
            rs.ObjectPrintWidth(line, self.width)
        self._pose.Origin = newPosition

    def setHeading(self, newHeading):
        self._pose.XAxis = newHeading

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
t.setPosition(-5, -5, -5)
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
