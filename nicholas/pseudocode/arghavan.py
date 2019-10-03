import math
import rhinoscriptsyntax as rs

"""
Target: write a program to draw a surface with a specific formula using small triangle meshes

formula:
    z = myfunction(x, y)
        where :
            x in range from x_min to x_max with x_slices (x_step = (x_max - x_min) / x_slices)
            y in range from y_min to y_max with y_slices (y_step = (y_max - y_min) / y_slices)

Pseudo-code:
    for y_i from 0 to y_slices - 1:
        p0 = [x_min, y_min + y_i * y_step]
        p1 = [x_min, y_min + (y_i + 1) * y_step]
        for x_i from  0 to x_slices - 1:
            p2 = [p0[0] + x_step, p0[1]] # px=P0[0]  py=p0[1]
            p3 = [p1[0] + x_step, p1[1]]
            calcaulate z for p0, p1, p2, p3 from formula
            draw a triangle with p0, p1 and p2
            draw a triangle with p1, p2 and p3
            p0 = p2
            p1 = p3

"""

def arghavan(x_min, x_max, x_slices, y_min, y_max, y_slices, formula):
    x_step = (x_max - x_min) / x_slices
    y_step = (y_max - y_min) / y_slices

    for y_i in range(0, y_slices):
        p0 = [x_min, y_min + y_i * y_step]
        p1 = [x_min, y_min + (y_i + 1) * y_step]
        for x_i in range(0, x_slices):
            p2 = [p0[0] + x_step, p0[1]]
            p3 = [p1[0] + x_step, p1[1]]
            setZ(p0, formula)
            setZ(p1, formula)
            setZ(p2, formula)
            setZ(p3, formula)
            drawTriangle(p0, p1, p2)
            drawTriangle(p1, p2, p3)
            p0 = p2
            p1 = p3

def setZ(point, formula):
    z = formula(point[0], point[1])
    if len(point) == 2:
        point.append(z)
    else:
        point[2] = z

def drawTriangle(p1, p2, p3):
    lines = [
        rs.AddLine(p1, p2),
        rs.AddLine(p2, p3),
        rs.AddLine(p1, p3)
    ]
    rs.AddPlanarSrf(lines)
    rs.DeleteObjects(lines)


arghavan(0, 10, 20, 0, 10, 20, lambda x, y: math.sqrt(x * y))
