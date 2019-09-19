import rhinoscriptsyntax as rs
from Rhino.RhinoMath import ToRadians
from Rhino.Geometry import Point3d, Vector3d
from System.Drawing import Color

class Turtle:
    
    _position = Point3d(0, 0, 0)
    _heading = Vector3d(1, 0, 0)  # Must be a unit vector
    _penDown = True
    _color = Color.FromArgb(0)
    
    def forward(self, distance):
        self._moveTo(self._position + (self._heading * distance))
    
    def back(self, distance):
        self.forward(-distance)
    
    def left(self, angle):
        self._heading.Rotate(ToRadians(angle), Vector3d(0, 0, 1))
    
    def right(self, angle):
        self.left(-angle)
        
    def setPosition(self, x, y=0, z=0):
        if isinstance(x, Point3d):
            self._moveTo(x)
        else:
            self._moveTo(Point3d(x, y, z))
            
    def setX(self, x):
        self._moveTo(Point3d(x, self._position.y, self._position.z))
            
    def setY(self, y):
        self._moveTo(Point3d(self._position.x, y, self._position.z))
            
    def setZ(self, z):
        self._moveTo(Point3d(self._position.x, self._position.y, z))
    
    def _moveTo(self, newPosition):
        if self._penDown:
            line = rs.AddLine(self._position, newPosition)
            rs.ObjectColor(line, self._color)
        self._position = newPosition
        
    def setHeading(self, newHeading):
        self._heading = newHeading
    
    def setColor(self, color):
        self._color = color
    
    def penUp(self):
        self._penDown = False
    
    def penDown(self):
        self._penDown = True


t = Turtle()
t.penUp()
t.setPosition(-15, 10, 0)
t.penDown()
t.forward(10)
t.left(45)
t.setColor(Color.FromArgb(255, 0, 0))
t.forward(10)
t.right(90)
t.setColor(Color.FromArgb(0, 0, 255))
t.forward(10)
