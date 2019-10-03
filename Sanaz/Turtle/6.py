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

a=50
for i in range(30):
    joey.forward(a), joey.left(90)
    a +=8


