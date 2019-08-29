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

for i in range(18):
    square(100)
    joey.left(20)


