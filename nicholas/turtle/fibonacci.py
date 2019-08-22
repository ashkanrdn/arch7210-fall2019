import argparse
import sys
import turtle

parser = argparse.ArgumentParser(description='Draw a regular polygon')
parser.add_argument('-n', '--num_segments', type=int, help='number of line segments')
parser.add_argument('-s', '--scale', type=float, help='scale factor')
argv = parser.parse_args()

n = argv.num_segments
if n < 1:
    print('Spiral must have at least 1 segment', file=sys.stderr)
    sys.exit(1)

s = argv.scale
if s < 1:
    print('Scale factor must be at least 1', file=sys.stderr)
    sys.exit(1)


t = turtle.Turtle()

current = 1
previous = 0

for i in range(n):
    t.forward(current * s)
    t.left(90)
    current, previous = current + previous, current

turtle.done()