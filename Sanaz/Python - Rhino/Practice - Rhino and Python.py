#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 1 ####################################################################
# Import the RhinoScript library to python as the variable rs

import rhinoscriptsyntax as rs
# Add a Point at cartesian coordinates (x, y, z) = (10, 10, 3)
rs.AddPoint([10,10,3])
# Add a Line from (0, 0, 0) to (3, -2, 0)
rs.AddLine([0,0,0], [13,12,0])



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 2 ####################################################################
# Import the RhinoScript library to python as the variable rs

import rhinoscriptsyntax as rs
# Disable Redraw so Rhino doesn't update every time it creates a new geometry
rs.EnableRedraw(False)
# Definition of variables for our loop/range
# Value at which the loop starts from
start = 0
# Value until which the loop goes to
to = 10
# Step value of the loop
step = 1
# Loop
for i in range(start,to,step):
     rs.AddPoint([i,0,0])
# Enable Redraw so Rhino draws the new geometry
rs.EnableRedraw(True);



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 3 ####################################################################

import rhinoscriptsyntax as rs
start = rs.GetPoint("Start of line")
if start:
  end = rs.GetPoint("End of line")
  if end: rs.AddLine(start,end)




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 4 ####################################################################

import math
import rhinoscriptsyntax as rs
scale_length = 25.5
number_of_lines = 24
#calculate
f = lambda n: scale_length - (scale_length / math.pow(2, (n/12)))
line_x = [f(n) for n in range(0,number_of_lines)]
#draw
rs.AddLine((0,0,0),(0,3,0)) #nut
for x in line_x:
  rs.AddLine((x,0,0),(x,3,0)) #lines





#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 5 ####################################################################

import rhinoscriptsyntax as rs
startPoint = [1.0, 2.0, 0.0]
endPoint = [4.0, 5.0, 0.0]
line1 = [startPoint, endPoint]
line1ID = rs.AddLine(line1[0],line1[1]) # Adds a line to the Rhino Document and returns an ObjectID
startPoint2 = [1.0, 4.0, 0.0]
endPoint2 = [4.0, 2.0, 0.0]
line2 = [startPoint2, endPoint2]
line2ID = rs.AddLine(line2[0],line2[1]) # Returns another ObjectID
int1 = rs.LineLineIntersection(line1ID,line2ID) # passing the ObjectIDs to the function.





#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 6 ####################################################################

import rhinoscriptsyntax as rs
ptOrigin = rs.GetPoint("Plane origin") 
ptX = rs.GetPoint("Plane X-axis", ptOrigin) 
ptY = rs.GetPoint("Plane Y-axis", ptOrigin) 
dX = rs.Distance(ptOrigin, ptX) 
dY = rs.Distance(ptOrigin, ptY) 
arrPlane = rs.PlaneFromPoints(ptOrigin, ptX, ptY) 
rs.AddPlaneSurface(arrPlane, 1.0, 1.0) 
rs.AddPlaneSurface(arrPlane, dX, dY)




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 7 ####################################################################

import rhinoscriptsyntax as rs
import math 
#Call rs.EnableRedraw(False)
for t in rs.frange(-50,50,1.25):  #-100,90,3
     arrPoint = [t * math.sin(5*t), t * math.cos(5*t),t]
     print(arrPoint)
     rs.AddPoint(arrPoint)
     #Call rs.EnableRedraw(True)



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 8 ####################################################################

import rhinoscriptsyntax as rs
def RecursiveCircle(pt, r):
    if r == 0:
        return 1
    else:
        rs.AddCircle(pt, r)
        return RecursiveCircle(pt, r-1)
pt = rs.GetPoint("Pick starting point")
RecursiveCircle(pt, 10)




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 9 ####################################################################

import rhinoscriptsyntax as rs
import math
 
#class definition
class MyPolygon:
    #polygon initialization or constructor method
    def __init__(self,radius,sides,origin):
        self.radius = radius
        self.sides = sides
        self.origin = origin
        origin = self.origin
        theta = (2*math.pi)/self.sides
        x = origin[0] + self.radius
        y = origin[1]
        z = origin[2]
        pt01 = rs.AddPoint(x,y,z);
        pts = []
        pts.append(pt01)
        degrees = theta*(180/math.pi)
        for i in range(1,self.sides):
            tempPt = pts[-1]
            newPt = rs.RotateObject(tempPt,origin,degrees,None,True)
            pts.append(newPt)
        pts.append(pt01)
        self.polygon = rs.AddPolyline(pts);
 
 
    def fillPolygon(self):
        return rs.AddPlanarSrf(self.polygon)
 
    def extrudePolygon(self,height):
        startPt = self.origin;
        newZ = self.origin[2]+height
        endPt = [self.origin[0],self.origin[1],newZ]
        return rs.ExtrudeCurveStraight(self.polygon, startPt, endPt)
 
 
 
userpt = rs.GetPoint("Pick a centerpoint")
polygon0 = MyPolygon(6,6,userpt)
polygon0.fillPolygon()
polygon0.extrudePolygon(5)
 
 
userpt = rs.GetPoint("Pick a centerpoint")
polygon1 = MyPolygon(8,12,userpt)
polygon1.fillPolygon()
polygon1.extrudePolygon(10)




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 10 ####################################################################

# This script will compute a bunch of cross-product vector based on a pointcloud 
import rhinoscriptsyntax as rs
def vectorfield():
    cloud_id = rs.GetObject("Input pointcloud", 2, True, True)
    if cloud_id is None: return 
    listpoints = rs.PointCloudPoints(cloud_id)
    base_point = rs.GetPoint("Vector field base point")
    if base_point is None: return
    for point in listpoints:
        vecbase = rs.VectorCreate(point, base_point)
        vecdir = rs.VectorCrossProduct(vecbase, (0,0,1))
        if vecdir:
            vecdir = rs.VectorUnitize(vecdir)
            vecdir = rs.VectorScale(vecdir, 2.0)
            AddVector(vecdir, point)




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Practice 11 ####################################################################
# This script will compute a bunch of cross-product vector based on a pointcloud 

import rhinoscriptsyntax as rs
idSurface = rs.GetObject("Surface to frame", 8, True, True)
intCount = rs.GetInteger("Number of iterations per direction", 20, 2)
uDomain = rs.SurfaceDomain(idSurface, 0) 
vDomain = rs.SurfaceDomain(idSurface, 1) 
uStep = (uDomain[1] - uDomain[0]) / intCount 
vStep = (vDomain[1] - vDomain[0]) / intCount
rs.EnableRedraw(False) 
for u in range(uDomain[0],uDomain[1], uStep):
    for v in range(vDomain[0],vDomain[1],vStep):
        pt = rs.EvaluateSurface(idSurface, [u, v])
        if rs.Distance(pt, rs.BrepClosestPoint(idSurface, pt)[0]) < 0.1:
            srfFrame = rs.SurfaceFrame(idSurface, [u, v])
            rs.AddPlaneSurface(srfFrame, 1.0, 1.0)

rs.EnableRedraw(True) 



