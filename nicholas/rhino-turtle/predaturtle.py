import random
import rhinoturtle
from Rhino.Geometry import Plane, Point3d
from System.Drawing import Color
import rhinoscriptsyntax as rs

reload(rhinoturtle)

class Predator(rhinoturtle.Turtle):

    def __init__(self):
        rhinoturtle.Turtle.__init__(self)

    def chase(self, prey):
        vector = prey.position - self.position
        distance = vector.Length
        self.heading = vector

        if distance < 8:
            self.forward(distance)
            return True

        self.forward(8)
        return False


class Prey(rhinoturtle.Turtle):

    def __init__(self):
        rhinoturtle.Turtle.__init__(self)

    def wander(self):
        distance = random.randint(1, 10)
        angle = random.randint(-45, 45)
        self.left(angle)
        self.forward(distance)


# Clear the board
rs.DeleteObjects(rs.AllObjects(select=True))

rabbit = Prey()
rabbit.penup()
rabbit.position = Point3d(20, 40, 0)
rabbit.color = Color.Blue
rabbit.pendown()

fox = Predator()
fox.color = Color.Red
#fox.position = Point3d(0, 0, 0)

rabbitIcon = rs.AddSphere(rabbit.position, 0.5)
rs.ObjectColor(rabbitIcon, rabbit.color)
def OnRabbitMove(vector):
    rs.MoveObject(rabbitIcon, vector)
rabbit.OnPositionChange.append(OnRabbitMove)

foxIcon = rs.AddCone(Plane.WorldXY, 2, 1)
rs.ObjectColor(foxIcon, fox.color)
def OnFoxMove(vector):
    rs.MoveObject(foxIcon, vector)
fox.OnPositionChange.append(OnFoxMove)

caught = False

while not caught:
    rabbit.wander()
    caught = fox.chase(rabbit)
    rs.Sleep(500)

rs.DeleteObject(rabbitIcon)
