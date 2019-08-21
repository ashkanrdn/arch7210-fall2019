import argparse
import math
import sys
import turtle

parser = argparse.ArgumentParser(description='Draw a regular polygon')
parser.add_argument('-n', '--num_sides', type=int, help='number of sides')
parser.add_argument('-r', '--radius', type=float, help='radius of polygon')
argv = parser.parse_args()

n = argv.num_sides
if n < 3:
    print('Polygon must have at least 3 sides', file=sys.stderr)
    sys.exit(1)

r = argv.radius
if r <= 0:
    print('Radius must be a positive number', file=sys.stderr)
    sys.exit(1)

t = turtle.Turtle()
screen = turtle.Screen()
screen.title(f'{n}-Sided Regular Polygon')

a = 360 / n
s = -r * math.sin(a) / math.sin((180 - a)/2)

t.penup()
t.goto(0, r)
t.pendown()

for i in range(n):
    t.forward(s)
    t.right(a)


turtle.done()
