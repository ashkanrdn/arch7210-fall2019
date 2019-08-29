#Original Code From: https://www.101computing.net/python-turtle-spirograph/
import turtle
from math import cos,sin
from time import sleep

#Turn backgorund black
window = turtle.Screen()
window.bgcolor("black")


#Create first turtle
frodo = turtle.Turtle()
frodo.hideturtle()
frodo._tracer(0)
frodo.speed(0)
frodo.pensize(2)
frodo.color("red")

#Create second turtle
gandalf = turtle.Turtle()
gandalf.hideturtle()
gandalf._tracer(0)
gandalf.speed(0)
gandalf.pensize(3)
gandalf.color("white")

#Control variables
R = 300
r = 25
d = 125

angle = 0

#Move pen to starting position
gandalf.penup()
gandalf.goto(R-r+d,0)
gandalf.pendown()

theta = 0.2
steps = int(6*3.14/theta)


#Loop that depending con the complexity of the shape requires and increased number of steps
for t in range(0,steps*5):
    #Exploration with the idea of a rainbow color spectrum
    #Honestly preffer it white
    #for colors in ["red", "orange", "yellow", "green", "blue", "indigo","violet" ]:
    frodo.clear()
    frodo.penup()
    frodo.setheading(0)
    frodo.goto(0,-R)
    frodo.pendown()
    frodo.hideturtle()
    
    angle+=theta
        
    x = (R - r) * cos(angle)
    y = (R - r) * sin(angle)
    frodo.penup()
    frodo.goto(x,y-r)
    frodo.pendown()
    frodo.hideturtle()
    frodo.penup()
    frodo.goto(x,y)
    frodo.dot(5)

    #Use of the parametric equations for a hypotrochoid
    #A hypotrochoid is a type of curve traced by a point attached to a circle of radius r rolling 
    # around the inside of a fixed circle of radius R, where the point is a distance d from the center of
    # the interior circle.
    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
    frodo.pendown()
    frodo.goto(x,y)
    frodo.dot(5)
    gandalf.goto(frodo.pos())
        
    frodo.getscreen().update() 
    sleep(0.05)

sleep(1)
frodo.clear()
frodo.getscreen().update()
turtle.done()