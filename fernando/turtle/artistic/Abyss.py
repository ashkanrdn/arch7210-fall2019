#Original Code from: www.101computing.net/python-turtle-spirograph/

import turtle
import time
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("black")
turtle.colormode(255)

def TurtleGeneration():
        Spirograph = turtle.Turtle()
        Spirograph.hideturtle()
        Spirograph.pensize(3)
        return Spirograph
  
#Function to create a spirograph
def MultiSpirograph(OuterRadius, InnerRadius, Distance, Angle, Color):

    Turtle = TurtleGeneration()
    TurtlePen = TurtleGeneration()
    TurtlePen.penup()
    TurtlePen.goto(OuterRadius-InnerRadius+Distance,0)
    TurtlePen.pendown()
    TurtlePen.color(Color)

    theta = 0.2
    steps = int(6*3.14/theta)

    for t in range(0,steps*8):
        Turtle.clear()
        Turtle.penup()
        Turtle.setheading(0)
        Turtle.goto(0,-OuterRadius)
        #Turtle.color("#999999")
        Turtle.pendown()
        Turtle.hideturtle()
        #Turtle.circle(R)
    
        Angle+=theta
        
        x = (OuterRadius - InnerRadius) * cos(Angle)
        y = (OuterRadius - InnerRadius) * sin(Angle)
        Turtle.penup()
        Turtle.goto(x,y-InnerRadius)
        Turtle.hideturtle()
        Turtle.color("black")
        Turtle.pendown()
        #Turtle.hideturtle()
        #Turtle.circle(r)
        Turtle.penup()
        Turtle.goto(x,y)
        #Turtle.dot(5)
        
        x = (OuterRadius - InnerRadius) * cos(Angle) + Distance * cos(((OuterRadius-InnerRadius)/InnerRadius)*Angle)
        y = (OuterRadius - InnerRadius) * sin(Angle) - Distance * sin(((OuterRadius-InnerRadius)/InnerRadius)*Angle)
        Turtle.pendown()
        Turtle.goto(x,y)
        #Turtle.dot(5)
        TurtlePen.goto(Turtle.pos())
#Variable to go through the loop
# X = the RGB value
# d is for distance from outer circle        
x = 255
d = 100
t = 3
r = 95
turtle.tracer(0)
while x > 0:
        MultiSpirograph(125, r, d, 0, (x,255,255))
        x = x - 20
        d = d + 60
        r = r + 5
turtle.done()