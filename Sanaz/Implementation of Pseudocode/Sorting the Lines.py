import rhinoscriptsyntax as rs
from math import asin, degrees  #https://developer.rhino3d.com/api/rhinoscript/math_methods/asin.htm

# a method for calculate the angle of any line 
# we need the length of the line, start point and end point coordination for this part
def angle_cal(length, st_point, ed_point):
    angles = []
    x_s = []
    x_e = []
    y_s = []
    y_e = []
    
    for i in range(0, len(length)):
        x_s.append(st_point[i][0])
        x_e.append(ed_point[i][0])
        y_s.append(st_point[i][1])
        y_e.append(ed_point[i][1])
        
        y = abs(y_s[i] - y_e[i])  #https://developer.rhino3d.com/guides/rhinoscript/primer-101/4-operators-and-functions/
        degree = degrees(asin(y / length[i]))  #https://blog.faradars.org/%D8%AA%D9%88%D8%A7%D8%A8%D8%B9-%D9%85%D8%B9%DA%A9%D9%88%D8%B3-%D9%85%D8%AB%D9%84%D8%AB%D8%A7%D8%AA%DB%8C/
        
        if (x_e[i] > x_s[i]) and (y_e[i] > y_s[i]):
            angles.append(degree)
        elif (x_e[i] < x_s[i]) and (y_e[i] > y_s[i]):
            angles.append(180 - degree)
        elif (x_e[i] < x_s[i]) and (y_e[i] < y_s[i]):
            angles.append(degree + 180)
        elif (x_e[i] > x_s[i]) and (y_e[i] < y_s[i]):
            angles.append(360 - degree)
        else:
            angles.append(degree)
    
    return angles
    
    
# the method for make the lines vertical
def to_vertical(objects, angles):
    for i in range(0, len(objects)):
        if angles[i] < 90:
            rs.RotateObject(objects[i], rs.CurveStartPoint(objects[i]), 90 - angles[i])
        elif 90 < angles[i] < 180:
            rs.RotateObject(objects[i], rs.CurveStartPoint(objects[i]), 90 - angles[i])
        elif 180 < angles[i] < 270:
            rs.RotateObject(objects[i], rs.CurveStartPoint(objects[i]), 270 - angles[i])
        elif 270 < angles[i] < 360:
            rs.RotateObject(objects[i], rs.CurveStartPoint(objects[i]), 270 - angles[i]) 
        elif angles[i] == 180 or angles[i] == 360:
            rs.RotateObject(objects[i], rs.CurveStartPoint(objects[i]), -90)
        else:
            continue
            
# sorting the lines # Bubble Sort (https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm)
def sort_lines(objects, length):
    for i in range(len(objects) - 1, 0, -1):
        for j in range(i):
            if length[j + 1] < length[j]:
                tmp = length[j + 1]
                length[j + 1] = length[j]
                length[j] = tmp
                
                tmp = objects[j + 1]
                objects[j + 1] = objects[j]
                objects[j] = tmp
                
                
# move the lines to the order
def order_draw(objects, st_point):
    for i in range(0, len(objects)):
        rs.MoveObject(objects[i], [i - rs.CurveStartPoint(objects[i])[0], 0, 0])
    
    
# move the lines to place them on x axis
def move_to_xAxis(objects, st_point):
    for i in range(0, len(objects)):
        tmp = [0, 0, 0]
        tmp[1] = -st_point[i][1]
        rs.MoveObject(objects[i], tmp)


# mirror the lines if needed
def mirror(objects, st_point, ed_point):
    for i in range(0, len(objects)):
        if st_point[i][1] > ed_point[i][1]:
            rs.MirrorObject(objects[i], [-1000, 0, 0], [1000, 0, 0])


if __name__ == "__main__":  #http://python.coderz.ir/lessons/l04.html
    # GUID of all objects in a list named 'objs'
    objs = rs.AllObjects()
    
    # start point, end point and the length of all lines 
    # stored in a special list separately
    st_points = []
    ed_points = []
    length = []
    
    for i in range(0, len(objs)):
        st_points.append(rs.CurveStartPoint(objs[i]))
        ed_points.append(rs.CurveEndPoint(objs[i]))
        length.append(rs.CurveLength(objs[i]))
    
    # calculate the angles in degree
    angles = angle_cal(length, st_points, ed_points)
    
    # move all the lines to place on the x axis
    move_to_xAxis(objs, st_points)
    
    # make the lines arrow to be vertical
    to_vertical(objs, angles)
    
    # mirror the lines by negative arrow
    mirror(objs, st_points, ed_points)
    
    # sorting the lines
    sort_lines(objs, length)
    
    # finally move the lines in the order
    order_draw(objs, st_points)
