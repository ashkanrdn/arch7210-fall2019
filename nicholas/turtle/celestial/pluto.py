import turtle
from astropy import units
from celestial import System

screen = turtle.Screen()
screen.bgcolor('#000000')
screen.tracer(0, 0)
system = System('@9', 200)

bodies = {
    'Pluto':    ('999', 1.307e22, 20, '#cc6633'),
    'Charon':   ('901', 1.53236e21, 10, '#ddbb88'),
    'Nyx':      ('902', 4.5e16, 4, 'white'),
    'Hydra':    ('903', 4.8e16, 4, 'white'),
    'Kerberos': ('904', 1.65e16, 4, 'white'),
    'Styx':     ('905', 7.5e15, 4, 'white'),
}

for name in bodies:
    id, mass, size, color = bodies[name]
    body = system.lookup(id, 'id')
    body.mass = mass * units.kilogram
    body.turtlesize(outline=size)
    body.pencolor(color)
    body.pendown()
    turtle.update()

while True:
    system.advance(1 * units.hour)
    turtle.update()
