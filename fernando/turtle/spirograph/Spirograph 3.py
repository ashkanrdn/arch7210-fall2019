#Original Code from: www.101computing.net/python-turtle-spirograph/
#GLobal variable
#Create turtle inside the function
#Keep in mind repeating turtles
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("black")

Spirograph = turtle.Turtle()
Spirograph.hideturtle()
Spirograph._tracer(0)
Spirograph.speed(0)
Spirograph.pensize(2)

Pen = turtle.Turtle()
Pen.hideturtle()
Pen._tracer(0)
Pen.speed(0)
Pen.pensize(3)
Pen.color("#f2f2f2")

#----------------------------------------

Spirograph1 = turtle.Turtle()
Spirograph1.hideturtle()
Spirograph1._tracer(0)
Spirograph1.speed(0)
Spirograph1.pensize(2)

Pen1 = turtle.Turtle()
Pen1.hideturtle()
Pen1._tracer(0)
Pen1.speed(0)
Pen1.pensize(3)
Pen1.color("#d9d9d9")

#----------------------------------------

Spirograph2 = turtle.Turtle()
Spirograph2.hideturtle()
Spirograph2._tracer(0)
Spirograph2.speed(0)
Spirograph2.pensize(2)

Pen2 = turtle.Turtle()
Pen2.hideturtle()
Pen2._tracer(0)
Pen2.speed(0)
Pen2.pensize(3)
Pen2.color("#bfbfbf")

#----------------------------------------

Spirograph3 = turtle.Turtle()
Spirograph3.hideturtle()
Spirograph3._tracer(0)
Spirograph3.speed(0)
Spirograph3.pensize(2)

Pen3 = turtle.Turtle()
Pen3.hideturtle()
Pen3._tracer(0)
Pen3.speed(0)
Pen3.pensize(3)
Pen3.color("#a6a6a6")

#----------------------------------------

Spirograph4 = turtle.Turtle()
Spirograph4.hideturtle()
Spirograph4._tracer(0)
Spirograph4.speed(0)
Spirograph4.pensize(2)

Pen4 = turtle.Turtle()
Pen4.hideturtle()
Pen4._tracer(0)
Pen4.speed(0)
Pen4.pensize(3)
Pen4.color("#8c8c8c")

#Control Variables
#Outter Circle Radius
R = 125

#Inner Circle Radius
r = 95

#Distance from outter circle center
d = 100
d1 = 160
d2 = 220
d3 = 280
d4 = 340

angle = 0

#Function to hide the spirograph once it ends
def HideSpirograph(Turtle):
    #Hide Spirograph
    Turtle.clear()
    Turtle.getscreen().update()
  
#Function to create a spirograph
def MultiSpirograph(TurtlePen, Turtle, OuterRadius, InnerRadius, Distance, Angle):

    TurtlePen.penup()
    TurtlePen.goto(OuterRadius-InnerRadius+Distance,0)
    TurtlePen.pendown()

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
        
        Turtle.getscreen().update() 
        sleep(0.05)

MultiSpirograph(Pen, Spirograph, R, r, d, angle)
MultiSpirograph(Pen1, Spirograph1, R, r, d1, angle)
#MultiSpirograph(Pen2, Spirograph2, R, r, d2, angle)
#MultiSpirograph(Pen3, Spirograph3, R, r, d3, angle)
#MultiSpirograph(Pen4, Spirograph4, R, r, d4, angle)

sleep(1)

HideSpirograph(Spirograph)
HideSpirograph(Spirograph1)
HideSpirograph(Spirograph2)
HideSpirograph(Spirograph3)
HideSpirograph(Spirograph4)

turtle.done()