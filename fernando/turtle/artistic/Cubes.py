import turtle
import random

#Create turtle
death = turtle.Turtle()

#Allow usuer to input value for number of iterations
cubes = input("Input the number of iterations desired ")
cubes = int(cubes)

#Pen size for outline and interior lines
outline = 2
interior = 1

#Loop to generate cubes
for i in range(cubes):
    #x and y values differ in order to get multiple variations
    #I suggest placing a value over 10 in order to ensure multiple cubes forming
    sizex = int(random.randint(-100,100))
    sizey = int(random.randint(-100,100))

    #Coordinates for new cube
    x_coordinate = int(random.randint(-50,50))
    y_coordinate = int(random.randint(-50,100))

    #If statement to make sure we do not get small cubes
    if -30 <= sizex <= 30 or -30 <= sizey <= 30: continue
    
    else:
        #Cube drawing
        death.pensize(outline)
        death.left(30)
        death.forward(sizex)
        death.left(60)
        death.forward(sizey)
        death.left(60)
        death.forward(sizey)
        death.left(60)
        death.forward(sizex)
        death.left(60)
        death.forward(sizey)
        death.left(60)
        death.forward(sizey)
        death.pensize(interior)
        death.setheading(90)
        death.forward(sizey)
        position = death.pos()
        death.left(60)
        death.forward(sizey)
        death.penup()
        death.goto(position)
        death.setheading(90)
        death.right(60)
        death.pendown()
        death.forward(sizex)
        death.setheading(0)
        death.penup()
        death.goto(x_coordinate,y_coordinate)
        death.pendown()

turtle.done()