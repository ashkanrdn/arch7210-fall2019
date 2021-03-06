import turtle
from astropy import units
from celestial import System

screen = turtle.Screen()
screen.bgcolor('#000000')
screen.tracer(0, 0)
solarSystem = System('@ssb', 1e6)

def create(type, id, color, size=12):
    body = solarSystem.lookup(id, type)
    body.pencolor(color)
    body.pendown()
    body.turtlesize(outline=size)
    turtle.update()
    return body

create('majorbody', '10', '#ffe000', 24) # Sun
create('majorbody', '199', '#999988')    # Mercury
create('majorbody', '299', '#33ff00')    # Venus
create('majorbody', '399', '#0099ff')    # Earth
create('majorbody', '499', '#ff0000')    # Mars

eros = create('smallbody', '433', '#aa9999', 4)
eros.mass = 6.687e15 * units.kilogram

while True:
    solarSystem.advance(24 * units.hour)
    turtle.update()
