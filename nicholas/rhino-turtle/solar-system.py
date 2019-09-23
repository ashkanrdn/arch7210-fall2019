from System.Drawing import Color
from Rhino.Geometry import Point3d, Vector3d
import rhinoscriptsyntax as rs
import celestial

# Clear the board
rs.DeleteObjects(rs.AllObjects(select=True))

solarSystem = celestial.System.fromJSON('./solar-system.json')

for i in range(365):
    solarSystem.advance(1)
    rs.Sleep(10)

for b in solarSystem.bodies:
    b.done()
