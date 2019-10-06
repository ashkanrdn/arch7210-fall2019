import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import Rhino.RhinoMath as rm
import math
import random
from System.Drawing import Color
import RhinoTurtle3D as rt
reload(rt)

NumMovements = 100
screenWidth = 500
screenHeight = 500
originBoundary = rg.Point3d((-screenWidth/2),int(-screenHeight/2), 0)

#This class contains vector calculations not provided in native turtle library
class Vec2DExpansion(rt.Turtle):

        #Calculate the angle between two coordinates / resturns the obtained angle
        def findAngle(self,positionA, positionB):
            """
            positionA : x and y coordinates of a turtle
            positionB : x and y coordinates of a turtle
            """
            angle = rs.Angle(positionA, positionB)
            return angle[0]

        #Calculate the distance between two points / retuns the obtained distance
        def pointDistance(self,positionA, positionB):
            """
            positionA : x and y coordinates of a turtle
            positionB : x and y coordinates of a turtle
            """
            distance = rs.Distance(positionA, positionB)
            return distance

#Create a turtle that has the ability to run around the canvas
class TurtleRunner(rt.Turtle):
    def __init__(self):
        rt.Turtle.__init__(self)
        self.penUp()

    #Make the turtle run randomly around the canvas
    def run(self):
        vector = rg.Vector3d(1,0,0)
        vector.Rotate(random.uniform(0,2*math.pi), rg.Vector3d.ZAxis)
        self.setHeading(vector)
        self.forward(10)
        
#Create a turtle that has the ability to follow another turtle around the canvas
class TurtleFollower(rt.Turtle):
    def __init__(self, x = 0, y = 0, z = 0):
        rt.Turtle.__init__(self)
        self._shape = rs.AddCylinder(rg.Plane.WorldXY, 4, 1, cap = True)
        #self._shape =rs.GetObject("Select the runner")
        self.setColor(255,0,0)
        self.penUp()
        self.goto(x,y,z)
        
        
    def follow(self, otherTurtle):
        """ 
        otherTurtle : other turtle objects
        """
        positionA = self.position()
        positionB = otherTurtle.position()

        #Calculate the angle from the two coordinates and make the turtle move forward
        angle = Vec2DExpansion().findAngle(positionA, positionB)
        vector = rg.Vector3d(1,0,0)
        vector.Rotate(rm.ToRadians(angle), rg.Vector3d.ZAxis)
        self.setHeading(vector)
        self.forward(10)
followers = []
bob = TurtleRunner()
for i in range(10):
    tina = TurtleFollower(random.uniform(-10,10), random.uniform(-10,10))
    followers.append(tina)
for i in range(20):
    bob.run()
    for follower in followers:
        follower.follow(bob)
    rs.Sleep(500)