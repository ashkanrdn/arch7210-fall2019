#Original code from www.101computing.net/python-turtle-spirograph/
#Optimize with a function and just adjust the size of the circles
import turtle
from math import cos,sin
from time import sleep

window = turtle.Screen()
window.bgcolor("black")

#First Turtle
Kenny = turtle.Turtle()
Kenny.hideturtle()
Kenny._tracer(0)
Kenny.speed(0)
Kenny.pensize(2)

#First Turtle Pen
Kyle = turtle.Turtle()
Kyle.hideturtle()
Kyle._tracer(0)
Kyle.speed(0)
Kyle.pensize(3)
#Color for the pen
Kyle.color("cyan")

#Second Turtle Pen
Stan = turtle.Turtle()
Stan.hideturtle()
Stan._tracer(0)
Stan.speed(0)
Stan.pensize(3)
#Color for the pen
Stan.color("magenta")

#Second Turtle
Eric = turtle.Turtle()
Eric.hideturtle()
Eric._tracer(0)
Eric.speed(0)
Eric.pensize(3)

#Control variables
#Radius of outer circle
R = 125

#Radius of inner circle
r = 95
smaller_r = 45

#Distance of inner circle from outer circle
d = 35
smaller_d = 135

angle = 45
angle2 = 90

#Move turtle to starting position
Kyle.penup()
Kyle.goto(R-r+d,0)
Kyle.pendown()

Eric.penup()
Eric.goto(R-smaller_r+smaller_d,0)
Eric.pendown()

theta = 0.2
steps = int(6*3.14/theta)

#Loop that depending con the complexity of the shape requires and increased number of steps
for t in range(0,steps*8):
    #Static circle
    Kenny.clear()
    Kenny.penup()
    Kenny.setheading(0)
    Kenny.goto(0,-R)
    Kenny.color("white")
    Kenny.pendown()
    Kenny.hideturtle()
    #Kenny.circle(R)

    Eric.clear()
    Eric.penup()
    Eric.setheading(0)
    Eric.goto(0,-R)
    Eric.color("white")
    Eric.pendown()
    Eric.hideturtle()
    #Eric.circle(R)

    angle+=theta

    x = (R - r) * cos(angle)
    y = (R - r) * sin(angle)
    Kenny.penup()
    Kenny.goto(x,y-r)
    Kenny.color("white")
    Kenny.pendown()
    Kenny.hideturtle()
    #Kenny.circle(r)
    Kenny.penup()
    Kenny.goto(x,y)
    #Kenny.dot(5)
    
    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)*2
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)*2
    Kenny.pendown()
    Kenny.goto(x,y)

    Kenny.dot(5)
    Kyle.goto(Kenny.pos())
    
    Kenny.getscreen().update() 
    sleep(0.05)

#The Second Turtle Begins Here 

    x = (R - smaller_r) * cos(angle2)
    y = (R - smaller_r) * sin(angle2)
    Eric.penup()
    Eric.goto(x,y-smaller_r)
    Eric.color("white")
    Eric.pendown()
    Eric.hideturtle()
    #Eric.circle(smaller_r)
    Eric.penup()
    Eric.goto(x,y)
    #Eric.dot(5)
    
    x = (R - smaller_r) * cos(angle) + smaller_d * cos(((R-smaller_r)/smaller_r)*angle)
    y = (R - smaller_r) * sin(angle) - smaller_d * sin(((R-smaller_r)/smaller_r)*angle)
    Eric.pendown()
    Eric.goto(x,y)

    #Eric.dot(5)
    Stan.goto(Eric.pos())
    
    Eric.getscreen().update() 
    sleep(0.05)

sleep(1)

#Hide Spirograph
Kenny.clear()
Kenny.getscreen().update()
Eric.clear()
Eric.getscreen().update()

turtle.done()