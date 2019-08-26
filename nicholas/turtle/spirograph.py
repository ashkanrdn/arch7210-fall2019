import argparse
import colorsys
import math
import turtle
import sys

# Hypotrochoid:
# x = (R - r) * cos(theta) + d * cos((R - r) / r * theta)
# y = (R - r) * cos(theta) - d * cos((R - r) / r * theta)

# Hypocycloid: Special case of Hypotrochoid where d == r
# x = (R - r) * cos(theta) + r * cos((R - r) / r * theta)
# y = (R - r) * sin(theta) - r * sin((R - r) / r * theta)

# Epitrochoid:
# x = (R + r) * cos(theta) - d * cos((R + r) / r * theta)
# y = (R + r) * sin(theta) - d * sin((R + r) / r * theta)

# Epicycloid: Special case of Epitrochoid where d == r
# x = (R + r) * cos(theta) - r * cos((R + r) / r * theta)
# y = (R + r) * sin(theta) - r * sin((R + r) / r * theta)

class Spirograph(turtle.Turtle):

    statorRadius = 0
    rotorRadius = 0
    penDistance = 0
    outside = False

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-R', '--statorRadius', type=int, required=True)
        parser.add_argument('-r', '--rotorRadius', type=int, required=True)
        parser.add_argument('-d', '--penDistance', type=int)
        parser.add_argument('-o', '--outside', action='store_true')
        parser.parse_args(namespace=self)

        if self.penDistance == 0:
            self.penDistance = self.rotorRadius

    # Number of complete revolutions around the stator required to reach max_theta
    def num_turns(self):
        return self.rotorRadius / math.gcd(self.rotorRadius, self.statorRadius)

    # Angle at which the curve returns to its starting point
    def max_theta(self):
        return 2 * math.pi * self.num_turns()

    def get_coordinates(self, theta):
        sign = 1 if self.outside else -1
        d1 = self.statorRadius + self.rotorRadius * sign
        d2 = d1 / self.rotorRadius * theta
        x = d1 * math.cos(theta) - self.penDistance * math.cos(d2) * sign
        y = d1 * math.sin(theta) - self.penDistance * math.sin(d2)
        return (x, y)
    
    def draw(self):
        self.penup()
        self.goto(self.get_coordinates(0))
        self.pendown()

        maxAngle = self.max_theta()
        step = math.radians(1)
        angle = step
        
        while angle < maxAngle:
            self.pencolor(colorsys.hsv_to_rgb(angle / maxAngle, 1, 1))
            self.goto(self.get_coordinates(angle))
            angle += step
        
        self.pencolor(colorsys.hsv_to_rgb(angle / maxAngle, 1, 1))
        self.goto(self.get_coordinates(angle))
        self._update()



spirograph = Spirograph()
spirograph.hideturtle()

screen = turtle.Screen()
screen.bgcolor('#000000')
screen.tracer(5, 0)

spirograph.parse_args()
spirograph.draw()

turtle.done()