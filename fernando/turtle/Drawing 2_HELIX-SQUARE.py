import turtle
import math
drawingboard = turtle.Turtle()

#Test of patters

#First value is outline / Second value is fill color
drawingboard.color("black" , "red")

x = 0
#Move to location away from center
drawingboard.begin_fill()
drawingboard.penup()
drawingboard.goto(0,-100)
drawingboard.pendown()

#Increase drawing speed
drawingboard.speed(100)

#Draw first line and turn
for i in range(100):
    drawingboard.forward(i*3) 
    #Original # is 59degrees
    #3D Boxes is #120degrees
    drawingboard.left(90) 
    
    #Draw the polygon / make the math so it adjust with any polygon
    for x in range(4):
        drawingboard.begin_fill()
        drawingboard.forward(100)
        drawingboard.right(90)
        x = x + 1
        drawingboard.end_fill()

#Move from ending position
drawingboard.penup()
drawingboard.forward(200)
drawingboard.pendown()
        
turtle.done()