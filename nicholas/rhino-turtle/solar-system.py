from System.Drawing import Color
from Rhino.Geometry import Point3d, Vector3d
import rhinoscriptsyntax as rs
import celestial

# Clear the board
rs.DeleteObjects(rs.AllObjects(select=True))

solarSystem = celestial.System(Point3d(0, 0, 0))

sun = celestial.Body(1.9885E+30)
sun.position = Point3d(-2.945500958785887E-03, 7.584503594761214E-03, -3.155516453004599E-07)
sun.velocity = Vector3d(-8.488126143298473E-06, -8.407680064266824E-07, 2.292805245948194E-07)
sun.color = Color.FromArgb(255, 255, 0)
sun.pendown()
solarSystem.add(sun)

earth = celestial.Body(5.97219E+24)
earth.position = Point3d(1.000642563219389E+00, -1.980756851030501E-02, -6.669589999111157E-07)
earth.velocity = Vector3d(1.869657383685140E-04, 1.713211466018630E-02, -1.172387796767108E-06)
earth.color = Color.FromArgb(0, 0, 255)
earth.pendown()
solarSystem.add(earth)

for i in range(365):
    solarSystem.advance(1)
    rs.Sleep(25)
