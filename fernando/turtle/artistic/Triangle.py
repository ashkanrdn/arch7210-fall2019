#Precedent Code - https://repl.it/talk/learn/Colorful-Circle-Spiral-Generator-Using-Python-Turtle/7532
import turtle
import math
import random

turtle.Screen().bgcolor('black')

Saitama = turtle.Turtle()
Saitama.speed(1000)
Saitama.color("white")
Saitama.pensize(2)

factor = random.randint(0,10)
multiplyer = input("Give me a number")
multiplyer = int(multiplyer)

for i in range(1):
    def drawTriangle(turtle,size):
        for i in range(15):
            for i in range(3):
                turtle.forward(size)
                turtle.left(120)
            size=size- factor+50
    def drawPattern(turtle,size,repeat):
        for i in range (repeat):
            drawTriangle(turtle,size)
            turtle.right(360/repeat)

    drawPattern(Saitama,100,multiplyer)
    Saitama.color("red")
    drawPattern(Saitama,20,multiplyer)
    Saitama.color("red")
    drawPattern(Saitama,0,multiplyer)

turtle.done()