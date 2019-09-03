import argparse
import colorsys
import math
import turtle

from spirograph_lib import Spirograph

parser = argparse.ArgumentParser()
parser.add_argument('-R', '--statorRadius', type=int, required=True)
parser.add_argument('-r', '--rotorRadius', type=int, required=True)
parser.add_argument('-n', '--numberOfCurves', type=int, required=True)
parser.add_argument('-d', '--distanceBetweenCurves', type=float, required=True)
args = parser.parse_args()

screen = turtle.Screen()
screen.bgcolor('#000000')
screen.tracer(0, 0)

curves = []

for i in range(args.numberOfCurves):
    c = Spirograph(args.statorRadius, args.rotorRadius, i*args.distanceBetweenCurves)
    c.pencolor(colorsys.hsv_to_rgb(i/args.numberOfCurves, 1, 1))
    c.start()
    curves.append(c)

more = True
while more:
    for c in curves:
        more = c.increment(math.radians(1))
    turtle.update()

turtle.done()