#playing with turtle graphics

import turtle
loadwindow = turtle.Screen()
joey = turtle.Turtle()
window = turtle.Screen()

#turn off draw mode
turtle.speed(0)

#create and run turle
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    def square(zel):
        joey.pendown()
        joey.forward(zel), joey.left(90)
        joey.forward(zel), joey.left(90)
        joey.forward(zel), joey.left(90)
        joey.forward(zel), joey.left(90)
        joey.penup()
    a=10
    for i in range(10):
        joey.forward(a), joey.left(90)
        a +=2









        
    


# wait for user to end 
