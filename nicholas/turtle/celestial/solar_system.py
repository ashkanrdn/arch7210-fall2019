import math
import turtle

from TurtleSystem import TurtleSystem
from MotionVector import MotionVector

UP = math.pi / 2
turtle.Screen().tracer(0, 0)

solarSystem = TurtleSystem(1e9)
sun = solarSystem.addBody(1.9885e30)

mercury = solarSystem.addBody(3.3011e23, MotionVector(47362, UP))
mercury.setposition(57909050000, 0)
mercury.pencolor('purple')
mercury.pendown()

venus = solarSystem.addBody(4.8675e24, MotionVector(35020, UP))
venus.setposition(108208000000, 0)
venus.pencolor('green')
venus.pendown()

earth = solarSystem.addBody(5.9722e24, MotionVector(29780, UP))
earth.setposition(149598023000, 0)
earth.pencolor('blue')
earth.pendown()

mars = solarSystem.addBody(6.4171e23, MotionVector(24007, UP))
mars.setposition(227939200000, 0)
mars.pencolor('red')
mars.pendown()

while True:
    solarSystem.advance(86000)
    turtle.update()


turtle.done()