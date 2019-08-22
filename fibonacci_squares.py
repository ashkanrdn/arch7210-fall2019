import argparse
import sys
import turtle

parser = argparse.ArgumentParser(description='Draw a regular polygon')
parser.add_argument('-n', '--num_squares', type=int, help='number of squares')
parser.add_argument('-s', '--scale', type=float, help='scale factor')
argv = parser.parse_args()

n = argv.num_squares
if n < 1:
    print('There must have at least 1 square', file=sys.stderr)
    sys.exit(1)

s = argv.scale
if s < 1:
    print('Scale factor must be at least 1', file=sys.stderr)
    sys.exit(1)

def drawSquare(length):
    t.right(90)
    t.pendown()
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.penup()
    t.backward(length)

turtle.Screen().title(f'{n} Fibonacci Squares')
t = turtle.Turtle()

current = 1
previous = 0

t.pendown()
t.forward(s)
t.penup()
t.backward(s)

for _ in range(n):
    drawSquare(current * s)
    current, previous = current + previous, current

turtle.done()