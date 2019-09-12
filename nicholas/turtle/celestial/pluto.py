import turtle
from astropy import units
from celestial import System

screen = turtle.Screen()
screen.bgcolor('#000000')
screen.tracer(0, 0)
system = System('@9', 200)

bodies = {
    'Pluto':    ('999', 1.303e22, 20),
    'Charon':   ('901', 1.586e21, 10),
    'Nyx':      ('902', 4.5e16, 4),
    'Hydra':    ('903', 4.8e16, 4),
    'Kerberos': ('904', 1.65e16, 4),
    'Styx':     ('905', 7.5e15, 4),
}

for name in bodies:
    id, mass, size = bodies[name]
    body = system.lookup(id, 'id')
    body.mass = mass * units.kilogram
    body.turtlesize(outline=size)
    body.pencolor('white')
    body.pendown()
    turtle.update()

while True:
    system.advance(1 * units.hour)
    turtle.update()
