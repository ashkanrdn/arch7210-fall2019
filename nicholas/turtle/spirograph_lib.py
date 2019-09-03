import math
import turtle

class Spirograph(turtle.Turtle):

    statorRadius = 0
    rotorRadius = 0
    penDistance = 0
    outside = False

    currentAngle = 0

    def __init__(self, R, r, d, outside = False):
        turtle.Turtle.__init__(self)
        self.statorRadius = R
        self.rotorRadius = r
        self.penDistance = d
        self.outside = outside
        self.hideturtle()

    # Number of complete revolutions around the stator required to reach max_theta
    def num_turns(self):
        return self.rotorRadius / math.gcd(self.rotorRadius, self.statorRadius)

    # Angle at which the curve returns to its starting point
    def max_theta(self):
        return 2 * math.pi * self.num_turns()

    # Returns the (x, y) coordinates of the curve at theta
    def get_coordinates(self, theta):
        sign = 1 if self.outside else -1
        d1 = self.statorRadius + self.rotorRadius * sign
        d2 = d1 / self.rotorRadius * theta
        x = d1 * math.cos(theta) - self.penDistance * math.cos(d2) * sign
        y = d1 * math.sin(theta) - self.penDistance * math.sin(d2)
        return (x, y)

    def start(self):
        self.penup()
        self.currentAngle = 0;
        self.goto(self.get_coordinates(0))
        self.pendown()

    def increment(self, angle):
        maxAngle = self.max_theta()
        self.currentAngle += angle
        if self.currentAngle < maxAngle:
            self.goto(self.get_coordinates(self.currentAngle))
            return True
        else:
            self.goto(self.get_coordinates(maxAngle))
            # self._update()
            return False
    
    # def draw(self):
    #     if self.currentAngle == 0:
    #         self.penup()
    #         self.goto(self.get_coordinates(0))
    #         self.pendown()
        
    #     maxAngle = self.max_theta()
    #     self.currentAngle += math.radians(1)
    #     self.pencolor(colorsys.hsv_to_rgb(self.currentAngle / maxAngle, 1, 1))

    #     if self.currentAngle < maxAngle:
    #         self.goto(self.get_coordinates(self.currentAngle))
    #         return True

    #     else:
    #         self.goto(self.get_coordinates(maxAngle))
    #         self._update()
    #         return False
