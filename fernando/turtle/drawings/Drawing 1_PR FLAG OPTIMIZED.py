import turtle
import math
#=======COLOR FLAG==========

pencil = turtle.Turtle()
pencil.hideturtle()

#Rectangle dimensions 
lenght = 45
height = 30

#Lines in flag
lines = 5

#Size multiplyer
x = 5

#Coordinates
x_coordinate = -100
y_coordinate = -10

#List of colors to use
skyblue = "#9AF4FF"
colors = ["red", "white", skyblue]

#Funtion to move the pen from one place to another without drawing
def MovePen(x_coordinate, y_coordinate):
    pencil.penup()
    pencil.goto(x_coordinate, y_coordinate)
    pencil.pendown()

MovePen(x_coordinate, y_coordinate)
line_height = height/lines*x

#Drawing the rectangle
for line in range(5):
    MovePen(x_coordinate,(y_coordinate + line_height*line))

    for sides in range(2):
        pencil.fillcolor(colors[line%2])
        pencil.begin_fill()
        pencil.forward(lenght*x)
        pencil.right(90)
        pencil.forward(line_height)
        pencil.right(90)
        pencil.end_fill()

#Drawing the triangle
pencil.fillcolor(colors[2])
pencil.begin_fill()
MovePen(x_coordinate, y_coordinate+height*x-line_height)
pencil.setheading(360)
pencil.right(30)
for side in range(3):
    pencil.forward(height*x)
    pencil.right(120)
pencil.end_fill()

#Move pen to location to for drawing the star
MovePen(x_coordinate+3*x,y_coordinate+10.8*x)
pencil.setheading(360)

#Draw the star
pencil.fillcolor(colors[1])
pencil.begin_fill()
for i in range(5):
    pencil.pencolor(colors[1])
    pencil.forward(9.36*x)
    pencil.right(144)
pencil.end_fill()

#=========BLACK AND WHITE FLAG==========
    
pen = turtle.Turtle()
pen.hideturtle()

#Coordinates
x_coordinateA = -100
y_coordinateA = -170

#List of colors to use
colorsA = ["black", "white"]
pencil.pencolor(colorsA[0])
MovePen(x_coordinateA, y_coordinateA)
line_height = height/lines*x

#Drawing the rectangle
for line in range(5):
    MovePen(x_coordinate,(y_coordinateA + line_height*line))

    for sides in range(2):
        pencil.fillcolor(colorsA[line%2])
        pencil.begin_fill()
        pencil.forward(lenght*x)
        pencil.right(90)
        pencil.forward(line_height)
        pencil.right(90)
        pencil.end_fill()

#Drawing the triangle
pencil.fillcolor(colorsA[0])
pencil.begin_fill()
MovePen(x_coordinateA, y_coordinateA+height*x-line_height)
pencil.setheading(360)
pencil.right(30)
for side in range(3):
    pencil.forward(height*x)
    pencil.right(120)
pencil.end_fill()

#Move pen to location to for drawing the star
MovePen(x_coordinateA+3*x,y_coordinateA+10.8*x)
pencil.setheading(360)

#Draw the star
pencil.fillcolor(colorsA[1])
pencil.begin_fill()
for i in range(5):
    pencil.pencolor(colorsA[1])
    pencil.forward(9.36*x)
    pencil.right(144)
pencil.end_fill()

turtle.done()