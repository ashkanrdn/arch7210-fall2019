import rhinoscriptsyntax as rs
from Rhino.Geometry import Point3d, Vector3d

#lines = rs.GetObjects("Select lines", filter=4)
lines = rs.AllObjects()

for i in range(len(lines)):
    p = Point3d(i, 0, 0)
    v = p - rs.CurveStartPoint(lines[i])
    rs.TransformObject(lines[i], rs.XformTranslation(v))
    a = rs.Angle(rs.CurveStartPoint(lines[i]), rs.CurveEndPoint(lines[i]))[0]
    rs.TransformObject(lines[i], rs.XformRotation2(90 - a, Vector3d.ZAxis, p))

start = 1
while start < len(lines):
    current = start
    while current > 0 and rs.CurveLength(lines[current-1]) > rs.CurveLength(lines[current]):
        rs.TransformObject(lines[current], rs.XformTranslation((-1, 0, 0)))
        rs.TransformObject(lines[current-1], rs.XformTranslation((1, 0, 0)))
        lines[current], lines[current-1] = lines[current-1], lines[current]
        current -= 1
        rs.Sleep(500)
    start += 1
