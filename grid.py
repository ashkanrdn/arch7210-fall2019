import argparse
import math
import sys
import turtle

parser = argparse.ArgumentParser(description='Draw a grid')
parser.add_argument('-r', '--rows', type=int, required=True, help='number of rows')
parser.add_argument('-c', '--columns', type=int, required=True, help='number of columns')
argv = parser.parse_args()

rows = argv.rows
if rows < 1:
    print('Grid must have at least one row', file=sys.stderr)
    sys.exit(1)

cols = argv.columns
if cols < 1:
    print('Grid must have at least one column', file=sys.stderr)
    sys.exit(1)

def drawLine(x1, y1, x2, y2):
    t.penup()
    t.hideturtle()
    t.goto(x1, y1)
    t.pendown()
    t.showturtle()
    t.goto(x2, y2)

t = turtle.Turtle()
screen = turtle.Screen()
screen.title(f'{rows}x{cols} Grid')
width, height = screen.screensize()

for i in range(cols + 1):
    x = width / cols * i
    drawLine(x, 0, x, height)

for i in range(rows + 1):
    y = height / rows * i
    drawLine(0, y, width, y)

turtle.done()