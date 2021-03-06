import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import Rhino.RhinoMath as rm
import math
from System.Drawing import Color

class Turtle:

    def __init__(self, origin = [0,0,0]):
        self._location = rg.Plane.WorldXY
        self._penDown = True
        self._lineweight = 0 
        self._color = Color.FromArgb(0,0,0)

    def lineweight(self):
        return self._lineweight

    def setLineWeight (self, weight):
        self._lineweight = weight

    def color(self):
        return self._color

    def setColor(self, r,g,b):
        self._color = Color.FromArgb(r,g,b)

    def position(self):
        return self._location.Origin

    def heading(self):
        return self._location.XAxis

    def _moveTowards(self, vector):
        if self._penDown:
            newLocation = self._location.Origin + vector
            line = rs.AddLine(self._location.Origin, newLocation)
            rs.ObjectColor(line, self._color)
            rs.ObjectPrintColor(line, self._color)
            rs.ObjectPrintWidth(line, self._lineweight)
        self._location.Translate(vector)

    def forward(self, distance):
        self._moveTowards(self.heading() * distance)

    def backwards(self, distance):
        self.forward(-distance)

    def setHeading(self, newHeading):
        self._location.XAxis = newHeading

    def left(self,angle):
        self._location.Rotate(rm.ToRadians(angle), self._location.ZAxis)

    def right(self,angle):
        self.left(-angle)

    def YAxisUp(self,angle):
        self._location.Rotate(rm.ToRadians(angle), self._location.YAxis)

    def YAxisDown(self,angle):
        self.YAxisUp(-angle)

    def XAxisUp(self,angle):
        self._location.Rotate(rm.ToRadians(angle), self._location.XAxis)

    def XAxisDown(self,angle):
        self.XAxisUp(-angle)

    def ZAxisUp(self,angle):
        self._location.Rotate(rm.ToRadians(angle), self._location.ZAxis)

    def ZAxisDown(self,angle):
        self.ZAxisUp(-angle)

    def goto(self, x, y, z=0):
        rs.MoveObject(self._location,(x,y,z))

    def penUp():
        self._penDown = False

    def penDown():
        self._penDown = True

#=================================CODE START===================================#

# Clear the board
rs.DeleteObjects(rs.AllObjects(select=True))

import random
elsa = Turtle()
colours = [255,255,0]
elsa.setColor(colours[0],colours[1],colours[2])
elsa.setHeading(rg.Vector3d(1,0,1))
c = 0
x = 0

while x < 100:
    idx = int(c)
    elsa.forward(20)
    elsa.right(98)
    x = x + 1
    c = c + 0.1
    elsa.ZAxisUp(36)
    #elsa.XAxisUp(36)
    elsa.right(36)
    elsa.setColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    
    
    





