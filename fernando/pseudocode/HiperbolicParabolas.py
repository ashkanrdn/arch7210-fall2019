import rhinoscriptsyntax as rs

#Editable variables to 
radius = 20
first_segments = 10
second_segments = 2
z_movement = 10
z_movement1 = 20
radius1 = 0.1

#Delete the objects that result from running the script, in order to not having to delete them manually
delete_objects = rs.DeleteObjects(rs.AllObjects())

#Select center point of pavilion
point = rs.AddPoint(0,0,0)
#Create circle around point
circle = rs.AddCircle(point, radius)

#Divide circle into point to create closed curved geometry / In this case it is a hexagon
circle_points = rs.DivideCurve(circle, first_segments, create_points = True)

#Create curve using the previous points and explode it to get the middle points of each lines
hexagon_curve = rs.AddPolyline(circle_points + [circle_points[0]])
hexagon_lines = rs.ExplodeCurves(hexagon_curve)
line_points = [rs.DivideCurve(lines, second_segments, create_points = True, return_points = True) for lines in hexagon_lines]


#Make list to store points
curve_points = []

#Move the center points
center_point = rs.CopyObject(point, (0,0,z_movement))
center_point_coordinates = rs.PointCoordinates(center_point)


#For loop to move the middle point to the top of the pavilion and to make a list of points to create the continous line of arches
for i in range(len(hexagon_lines)):

    #Move the middle points
    moved_points = [rs.MoveObject(line_points[i][1], (0,0,z_movement1))]
    moved_points_coordinates = [rs.PointCoordinates(moved_points)]
    
    #From here the list is created
    starting_Pt = rs.CurveStartPoint(hexagon_lines[i])
    curve_points.append(starting_Pt)
    curve_points.append(moved_points_coordinates[0])
    end_Pt = rs.CurveEndPoint(hexagon_lines[i])
    curve_points.append(end_Pt)
    
#Add last point on the list to make sure all the arches have form
curve_points.append(curve_points[0])

#Create arches around pavilion / Color arcs to see better
arches = rs.AddCurve(curve_points, 2)

#rs.AddSweep1(arches,lines[0][1],closed = True)
circle1 = rs.AddCircle(center_point, radius1)
rs.AddLoftSrf([arches,circle1])
