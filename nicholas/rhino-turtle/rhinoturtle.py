import rhinoscriptsyntax as rs
from Rhino.RhinoMath import ToRadians
from Rhino.Geometry import Plane, Point3d, Vector3d
from System.Drawing import Color

class Turtle:
    
    def __init__(self):
        self._pose = Plane.WorldXY
        self._penDown = True
        self._color = Color.FromArgb(0)
        self._weight = 0
    
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
            rs.ObjectColor(line, self._color)
            rs.ObjectPrintColor(line, self._color)
            rs.ObjectPrintWidth(line, self._weight)
        self._pose.Translate(vector)
    
    def moveTo(self, newPosition):
        if self._penDown:
            line = rs.AddLine(self._pose.Origin, newPosition)
            rs.ObjectColor(line, self._color)
            rs.ObjectPrintColor(line, self._color)
            rs.ObjectPrintWidth(line, self._weight)
        self._pose.Origin = newPosition
        
    def setHeading(self, newHeading):
        self._pose.XAxis = newHeading
    
    def setColor(self, color):
        self._color = color
    
    def penUp(self):
        self._penDown = False
    
    def penDown(self):
        self._penDown = True
    
    def setWeight(self, weight):
        self._weight = weight



# Clear the board
rs.DeleteObjects(rs.AllObjects(select=True))

red = Color.FromArgb(255, 0, 0)
green = Color.FromArgb(0, 255, 0)
blue = Color.FromArgb(0, 0, 255)

t = Turtle()
t.penUp()
t.setPosition(-5, -5, -5)
t.penDown()

t.setColor(red)
t.forward(10)
t.up(90)

t.setWeight(1)
t.setColor(blue)
t.forward(10)
t.left(90)

t.setWeight(2)
t.setColor(green)
t.forward(10)
t.up(90)

t.setWeight(3)
t.setColor(red)
t.forward(10)
t.left(90)

t.setWeight(4)
t.setColor(blue)
t.forward(10)
t.up(90)

t.setWeight(5)
t.setColor(green)
t.forward(10)
t.left(90)
