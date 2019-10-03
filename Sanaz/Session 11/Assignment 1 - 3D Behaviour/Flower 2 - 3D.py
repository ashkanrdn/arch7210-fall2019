import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import Rhino.RhinoMath as rm
import math
import random
from System.Drawing import Color

class Turtle:
    
    def __init__(self, origin = [0,0,0]):
        self._location = rg.Plane.WorldXY
        self._penDown = True
        self._lineweight = 0 
        self._color = Color.FromArgb(0,0,0)
        #self._shape = rs.AddSphere(self._location.Origin, 2)
        self._shape = rs.GetObject("Select the turtle")
        
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
            rs.MoveObject(self._shape, newLocation)
        self._location.Translate(vector)
        rs.MoveObject(self._shape, self._location.Origin)
        
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
    
    def goto(self, x, y, z=0):
        self._location.Origin = rg.Point3d(x,y,z)
        rs.MoveObject(self._shape, (x,y,z))
     
    def penUp(self):
        self._penDown = False
   
    def penDown(self):
        self._penDown = True
        
#=======TURTLE FOLLOWER / RUNNER ==============



#================CODE START====================
if __name__ == "__main__": 

    # Clear the board
    rs.DeleteObjects(rs.AllObjects(select=True))
    
    elsa = Turtle()
    colours = [255,255,0]
    elsa.setColor(colours[0],colours[1],colours[2])
    elsa.setHeading(rg.Vector3d(1,0,1))
    for i in range(10):
        for i in range(2):
            elsa.forward(100)
            elsa.right(60)
            elsa.forward(100)
            elsa.right(120)
        elsa.YAxisUp(36)
        elsa.XAxisUp(36)
        elsa.right(36)
        elsa.setColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

