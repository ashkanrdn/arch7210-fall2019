import turtle
import math
pencil = turtle.Turtle()

#This was more of a test of colors & movement

#X helps increase the whole size of the drawing
x = 2
#List of colors to use
colors = ["red", "cyan", "white"]

#Make square
pencil.forward(45*x)
pencil.left(90)
pencil.forward(30*x)
pencil.left(90)
pencil.forward(45*x)
pencil.left(90)
pencil.forward(30*x)

#Make triangle
pencil.fillcolor(colors[1])
pencil.begin_fill()
pencil.left(90+33.69)
pencil.forward(27.042*x)
pencil.left(112.62)
pencil.forward(27.042*x)
pencil.setheading(360)
pencil.end_fill()

#Make the lines from top to bottom

#Make adjustments for pen
pencil.fillcolor(colors[0])
pencil.begin_fill()
pencil.penup()
pencil.forward(45*x)
pencil.right(90)
pencil.forward(6*x)
pencil.right(90)
pencil.pendown()

#Draw the line
pencil.forward(36*x)
pencil.end_fill()

#Make adjustments for pen
pencil.penup()
pencil.backward(36*x)
pencil.setheading(270)
pencil.forward(6*x)
pencil.setheading(180)
pencil.pendown()

#Draw the line
pencil.forward(27*x)

#Make adjustments for pen
pencil.fillcolor(colors[0])
pencil.begin_fill()
pencil.pencolor(colors[0])
pencil.penup()
pencil.backward(27*x)
pencil.setheading(270)
pencil.forward(3*x)
pencil.setheading(180)
pencil.pendown()

#Draw the line
pencil.forward(22.5*x)
pencil.end_fill()

#Make adjustments for pen
pencil.fillcolor(colors[0])
pencil.begin_fill()
pencil.pencolor("black")
pencil.penup()
pencil.backward(22.5*x)
pencil.setheading(270)
pencil.forward(3*x)
pencil.setheading(180)
pencil.pendown()

#Draw the line
pencil.forward(27*x)
pencil.end_fill()

#Make adjustments for pen
pencil.fillcolor(colors[0])
pencil.begin_fill()
pencil.penup()
pencil.backward(27*x)
pencil.setheading(270)
pencil.forward(6*x)
pencil.setheading(180)
pencil.pendown()

#Draw the line
pencil.forward(36*x)

#Make adjustments for pen
pencil.fillcolor(colors[0])
pencil.begin_fill()
pencil.penup()
pencil.backward(36*x)
pencil.setheading(270)
pencil.forward(6*x)
pencil.setheading(180)
pencil.pendown()

#Draw line
pencil.forward(45*x)
pencil.end_fill()

#Move pen to location to for drawing the star
pencil.penup()
pencil.goto(3*x,16.8*x)
pencil.pendown()
pencil.setheading(360)

#Draw the star
pencil.fillcolor(colors[2])
pencil.begin_fill()
for i in range(5):
    pencil.pencolor(colors[2])
    pencil.forward(9.36*x)
    pencil.right(144)
pencil.end_fill()

#Analyse code and which parts are repetition

turtle.done()