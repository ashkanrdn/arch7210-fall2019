#playing with turtle graphics

import turtle

#create window
loadwindow = turtle.Screen()
turtle.colormode(255)

#turn off draw mode
turtle.speed(0)

sides = 5

#create and run turle
def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(90)

for i in range(100):
    shape(5*i, sides)
    turtle.left(i)


   
# wait for user to end 
