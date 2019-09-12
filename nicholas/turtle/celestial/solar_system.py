import math
import turtle

from TurtleSystem import TurtleSystem
from MotionVector import MotionVector
from horizons import HorizonsLookup

UP = math.pi / 2
turtle.Screen().tracer(0, 0)
solarSystem = TurtleSystem(1e9)

def create(id, color,):
    data = HorizonsLookup(id, '@ssb')
    body = solarSystem.addBody(data.mass(), data.velocity())
    body.setposition(data.position())
    body.pencolor(color)
    body.pendown()
    turtle.update()

create('10', 'yellow')  # Sun
create('199', 'purple') # Mercury
create('299', 'green')  # Venus
create('399', 'blue')   # Earth
create('499', 'red')    # Mars

while True:
    solarSystem.advance(3600)
    turtle.update()
