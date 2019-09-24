import random
import rhinoturtle
from Rhino.Geometry import Plane, Point3d
from System.Drawing import Color
import rhinoscriptsyntax as rs

reload(rhinoturtle)

class Predator(rhinoturtle.Turtle):

    def __init__(self, maxSpeed):
        rhinoturtle.Turtle.__init__(self)
        self.maxSpeed = maxSpeed

    def chase(self, prey):
        vector = prey.position - self.position
        distance = vector.Length
        self.heading = vector

        if distance < self.maxSpeed:
            self.forward(distance)
            return True

        self.forward(self.maxSpeed)
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

fox = Predator(8)
fox.color = Color.Red


rabbitIcon = rs.AddSphere(rabbit.position, 0.5)
rs.ObjectColor(rabbitIcon, rabbit.color)
rabbit.decorate(rhinoturtle.Decorator(rabbitIcon))

foxIcon = rs.AddCone(Plane.WorldXY, 2, 1)
rs.ObjectColor(foxIcon, fox.color)
fox.decorate(rhinoturtle.Decorator(foxIcon))

caught = False

while not caught:
    rabbit.wander()
    caught = fox.chase(rabbit)
    rs.Sleep(500)

rs.DeleteObject(rabbitIcon)
