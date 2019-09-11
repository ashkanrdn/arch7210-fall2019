import argparse
import colorsys
import math
import turtle

from spirograph_lib import Spirograph

parser = argparse.ArgumentParser()
parser.add_argument('-R', '--statorRadius', type=int, required=True)
parser.add_argument('-d', '--penDistance', type=int, required=True)
parser.add_argument('-c', '--curveDivisors', type=int, nargs='+', required=True)
args = parser.parse_args()

screen = turtle.Screen()
screen.bgcolor('#000000')
screen.tracer(0, 0)

curves = []
numCurves = len(args.curveDivisors)

for i in range(numCurves):
    d = args.curveDivisors[i]
    c = Spirograph(args.statorRadius, math.floor(args.statorRadius / d), args.penDistance)
    c.pencolor(colorsys.hsv_to_rgb(i / numCurves, 1, 1))
    c.pensize(numCurves - i)
    c.start()
    curves.append(c)

more = True
while more:
    for c in curves:
        more = c.increment(math.radians(1))
    turtle.update()

turtle.done()