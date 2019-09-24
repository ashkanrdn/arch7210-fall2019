from System.Drawing import Color
from Rhino.Geometry import Plane, Point3d, Vector3d
import rhinoscriptsyntax as rs
import rhinoturtle
import celestial
import math


def createSphereDecorator(body):
    sphere = rs.AddSphere(body.position, 0.05)
    rs.ObjectColor(sphere, body.color)
    return rhinoturtle.Decorator(sphere)

def createLabelDecorator(body):
    text = rs.AddTextDot(body.name, body.position + Vector3d.ZAxis * 0.25)
    rs.ObjectColor(text, body.color)
    return rhinoturtle.Decorator(text)


# Clear the board
rs.DeleteObjects(rs.AllObjects(select=True))

solarSystem = celestial.System.fromJSON('./solar-system.json')

for body in solarSystem.bodies:
    body.decorate(createSphereDecorator(body))
    body.decorate(createLabelDecorator(body))

for i in range(730):
    solarSystem.advance(1)
    rs.Sleep(10)
