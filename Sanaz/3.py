import turtle
joey = turtle.Turtle()
window = turtle.Screen()
def square(zel):
    joey.pendown()
    joey.forward(zel), joey.left(90)
    joey.forward(zel), joey.left(90)
    joey.forward(zel), joey.left(90)
    joey.forward(zel), joey.left(90)
    joey.penup()
    
joey.penup()
joey.goto(-200, 0)
square(50)

joey.goto(-100, 0)
square(50)

joey.goto(-0, 0)
square(50)

joey.goto(100, 0)
square(50)

joey.goto(200, 0)
square(50)
