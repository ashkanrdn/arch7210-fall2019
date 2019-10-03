# Import

import random
import time
import turtle
from turtle import Turtle
from random import randint #randint is a function that is part of the random module.The official Python documentation on it is at random.randint(a, b).It returns a pseudorandom integer between a and b , inclusive. You must import the function in some manner, in order to use it.  

# Window Setup
window = turtle.Screen()
window.title("TURTLES")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(1)
turtle.penup()
turtle.setpos(-200, 200) #turtle.setpos(x, y=None)
turtle.write("TURTLES", font=("Arial", 30, "bold"))
turtle.penup()

# COLOR RECTANGLE
turtle.setpos(-400, -180)
turtle.color("purple")
turtle.begin_fill() #Call just before drawing a shape to be filled.
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()  #Fill the shape drawn after the last call to begin_fill()

# fINISH LINE 
stamp_size = 20  #Move and draw / turtle.stamp Stamp a copy of the turtle shape onto the canvas at the current turtle position
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size) #turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None) // turtle.shapesize(5, 5, 12)
turtle.penup()

#i,j
for i in range(10):
    turtle.setpos(finish_line, (150 - (i * square_size * 2)))  #150 = y (Finish Line)/ *2 = development of squares
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line + square_size, ((150 - square_size) - (j * square_size * 2)))
    turtle.stamp()

turtle.hideturtle()

# TURTLE 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("black") #color 
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)#coordinate 
turtle1.pendown()

# TURTLE 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("cyan")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

# TURTLE 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("magenta")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()

# TURTLE 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("yellow")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()

time.sleep(1) #puse the game for 1 second before starting the race

# MOVE THE TURTLE
for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))

#CONGRADULATIONS    
t = turtle.Pen()
t.speed(0)
def mycircle(red, green, blue):
	t.color(red, green, blue)
	t.begin_fill()
	x = random.randint(10,100) #set random move values: random = random.randint(50,100)  #generate random direction: rnumber = random.randint(1,4)
	t.circle(x) # draw a circle of random radius
	t.end_fill()
	t.up() # pick up pen
	y = random.randint(0,360)
	t.seth(y) # set heading to random direction     #turn a random direction 1 // turtle.setheading(rnumber)
	# t.xcor() is turtle's x; t.ycor() is turtle's y
	if t.xcor() < -300 or t.xcor() > 300:
		t.goto(0, 0) # this is the center 
	elif t.ycor() < -300 or t.ycor() > 300:
		t.goto(0, 0) # this is the center 
	z = random.randint(0,100)
	t.forward(z) # move a random number of pixels
	t.down() # pen down

for i in range(0, 100):
	a = random.randint(0,100)/100.0
	b = random.randint(0,100)/100.0
	c = random.randint(0,100)/100.0
	mycircle(a, b, c) # feed a random color to the function

t.setpos(0, 0) #turtle.setpos(x, y=None)
t.color("white")
t.penup()
t.write("YOU WON", font=("Arial", 30, "bold"))
t.penup()
time.sleep(1)

turtle.exitonclick()

