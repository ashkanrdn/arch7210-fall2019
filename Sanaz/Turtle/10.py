#playing with turtle graphics

import turtle

#create window
loadwindow = turtle.Screen()
turtle.colormode(255)

#turn off draw mode
turtle.speed(0)

sides = 6

#create and run turle
def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)

for i in range(100):
    shape(i, i)
    turtle.left(i)


   
# wait for user to end 
