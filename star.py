import argparse
import math
import sys
import turtle

parser = argparse.ArgumentParser(description='Draw a star')
parser.add_argument('-n', '--num_vertices', type=int, help='number of vertices')
parser.add_argument('-r', '--radius', type=float, help='radius of star')
argv = parser.parse_args()

n = argv.num_vertices
if n < 5:
    print('Star must have at least 5 vertices', file=sys.stderr)
    sys.exit(1)
if n % 2 == 0:
    print('Star must have an odd number of vertices', file=sys.stderr)
    sys.exit(1)

r = argv.radius
if r <= 0:
    print('Radius must be a positive number', file=sys.stderr)
    sys.exit(1)

t = turtle.Turtle()
screen = turtle.Screen()
screen.title(f'{n}-Pointed Star')

a = 360 / n
s = -r * math.sin(180 - a/2) / math.sin(180 - a/4)

t.pendown()

for i in range(n):
    t.forward(s)
    t.right(180 - a/2)


turtle.done()
