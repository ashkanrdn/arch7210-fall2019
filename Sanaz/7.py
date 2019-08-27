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

a=20
for i in range(40):
    joey.forward(a), joey.left(90)
    a +=5
    joey.left(10)


