import argparse
import turtle

t = turtle.Turtle()
t.hideturtle()
t.setheading(90)

screen = turtle.Screen()
screen.tracer(1, 0)

def branch(t, length):
    t.forward(length)

    length = length * 0.55
    if length > 1:

        left = t.clone()
        left.left(30)
        branch(left, length)

        right = t.clone()
        right.right(30)
        branch(right, length)

branch(t, 200)
turtle.done()