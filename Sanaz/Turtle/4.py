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

square(200)
square(175)
square(150)
square(125)
square(100)


