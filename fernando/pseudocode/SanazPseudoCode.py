import rhinoscriptsyntax as rs
rs.DeleteObjects(rs.AllObjects())

division = 10
point = rs.AddPoint(0,0,0)
outterCircle = rs.AddCircle(point, 10)
innerCircle = rs.AddCircle(point, 8)
rs.RotateObject(outterCircle, point, 90)
rs.RotateObject(innerCircle, point, 90)
dividedPoints = rs.DivideCurve(outterCircle, division, True)
dividedPointsInner = rs.DivideCurve(innerCircle, division, True)

lines1 = []
lines2 = []
lines3 = []
lines4 = []

for i in range(len(dividedPoints)):
    lines1.append(rs.AddLine(dividedPoints[i],dividedPoints[(i+3)%division]))
    lines2.append(rs.AddLine(dividedPoints[i],dividedPoints[(i+4)%division]))
    lines3.append(rs.AddLine(point, dividedPoints[i]))
for j in range(len(lines1)):
    intersection = rs.LineLineIntersection(lines1[j], lines1[(j+2)%division])
    rs.AddLine(point,intersection[0])

lines4.append(dividedPoints[0])
x = rs.LineLineIntersection(lines1[0],lines2[7])
lines4.append(rs.AddPoint(x[0]))
z = rs.LineLineIntersection(lines3[0],lines2[7])
lines4.append(rs.AddPoint(z[0]))
y = rs.LineLineIntersection(lines1[7], lines2[9])
lines4.append(rs.AddPoint(y[0]))
lines4.append(dividedPoints[0])

polylines = []
polyline = rs.AddCurve(lines4, 1)
polylines.append(polyline)

angle = rs.Angle2(lines3[0], lines3[1])
rotation = angle[0]

#rs.ObjectColor(innerCircle, color=(255,0,0))
#rs.ObjectColor(outterCircle, color=(255,0,0))

for t in range(len(dividedPoints)):
    polylines.append(rs.RotateObject(polyline, point, rotation*t, axis=None, copy=True))
    rs.ObjectColor(polyline, color=(255,0,0))
    
white = rs.CreateColor(255,255,255)

translation = rs.VectorCreate(dividedPoints[1], dividedPointsInner[6])
rs.CopyObjects(polylines, translation)
translation = rs.VectorCreate(dividedPoints[4], dividedPointsInner[9])
rs.CopyObjects(polylines, translation)
translation = rs.VectorCreate(dividedPoints[6], dividedPointsInner[1])
rs.CopyObjects(polylines, translation)
translation = rs.VectorCreate(dividedPoints[9], dividedPointsInner[4])
rs.CopyObjects(polylines, translation)
    #rs.CopyObjects(outterCircle, translation)
    #rs.CopyObjects(innerCircle, translation)

rs.DeleteObjects(rs.ObjectsByColor(white))

