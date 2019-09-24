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
        self.OnPositionChange = []


    # Position properties and methods

    @property
    def position(self):
        """The turtle's current position."""
        return self._pose.Origin

    @position.setter
    def position(self, newPosition):
        if self._penDown:
            self._drawLine(newPosition)

        for callback in self.OnPositionChange:
            callback(newPosition - self._pose.Origin)

        self._pose.Origin = newPosition

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


    # Heading properties and methods

    @property
    def heading(self):
        """The turtle's current heading."""
        return self._pose.XAxis

    @heading.setter
    def heading(self, newHeading):
        vector = Vector3d(newHeading)
        vector.Unitize()
        self._pose.XAxis = vector

    def left(self, angle):
        """Turn the turtle `angle` degrees to the left."""
        self._pose.Rotate(ToRadians(angle), self._pose.ZAxis)

    def right(self, angle):
        """Turn the turtle `angle` degrees to the right."""
        self.left(-angle)

    def down(self, angle):
        """Turn the turtle downward by `angle` degrees."""
        self._pose.Rotate(ToRadians(angle), self._pose.YAxis)

    def up(self, angle):
        """Turn the turtle upward `angle` degrees."""
        self.down(-angle)

    def rollLeft(self, angle):
        """Roll the turtle `angle` degrees to the left."""
        self._pose.Rotate(ToRadians(angle), self._pose.XAxis)

    def rollRight(self, angle):
        """Roll the turtle `angle` degrees to the right."""
        self.left(-angle)


    # Movement methods

    def move(self, vector):
        """Move the turtle according to the given vector."""
        if self._penDown:
            self._drawLine(self._pose.Origin + vector)

        for callback in self.OnPositionChange:
            callback(vector)

        self._pose.Translate(vector)

    def _drawLine(self, endPoint):
        """Draw a line from the turtle's current position to `endPoint`."""
        line = rs.AddLine(self._pose.Origin, endPoint)
        rs.ObjectColor(line, self.color)
        rs.ObjectPrintColor(line, self.color)
        rs.ObjectPrintWidth(line, self.width)

    def forward(self, distance):
        """Move the turtle forward by the specified `distance`."""
        self.move(self.heading * distance)

    def back(self, distance):
        """Move the turtle backward by the specified `distance`."""
        self.forward(-distance)


    # Pen control methods

    def pendown(self):
        """Put the pen down so the turtle draws when moving."""
        self._penDown = True

    def penup(self):
        """Pull the pen up so the turtle does not draw when moving."""
        self._penDown = False
