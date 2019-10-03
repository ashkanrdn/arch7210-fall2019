import rhinoscriptsyntax as rs

#allObjs = rs.AllObjects()
#rs.DeleteObjects(allObjs)

class Turtle:
    def __init__(self, pos = [0,0,0], heading = [1,0,0],color=[0,0,0],weight=0.5):
        self.color = color
        self.weight = weight
        self.heading = heading
        self.point = rs.AddPoint(pos)
        pointPos = rs.PointCoordinates(self.point)
        self.direction = rs.VectorCreate(heading, pointPos)
        self.lines = []
        self.draw = True

    def forward(self,magnitude):
        movement = rs.VectorScale(self.direction, magnitude)
        prevPos = rs.PointCoordinates(self.point)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        line = self.drawLine(prevPos,currentPos)
        return line

    #
    def left(self,angle,axis=[0,0,1]):

        self.direction = rs.VectorRotate(self.direction, angle, axis)
        print(self.direction)

    #
    def right(self,angle,axis=[0,0,1]):
        self.direction = rs.VectorRotate(self.direction, -angle, axis)
        print(self.direction)

    def goto(self, x, y, z=0):
        prevPos = rs.PointCoordinates(self.point)
        movement = rs.VectorCreate([x,y,z],prevPos)
        rs.MoveObject(self.point,movement)
        currentPos = rs.PointCoordinates(self.point)
        line = self.drawLine(prevPos,currentPos)
        return line

    #
    def drawLine(self, p1, p2):
        if self.draw:
            l=rs.AddLine(p1,p2)
            rs.ObjectColor(l,self.color)
            rs.ObjectPrintWidth(l,self.weight)
            return l
        else:
            pass

    #
    def penUp(self):
        self.draw = False

    #
    def penDown(self):
        self.draw = True

    #
    def setWeight(self, weight):
        self.weight= weight

    #
    def setColor(self, color):
        colorList = Turtle.getColorList()
        if type(color) == list:
            self.color = color
        if isinstance(color, str):
            self.color = colorList[color]

    #
    def grid(self , sqr,x ,y):
        xpldCrv = rs.ExplodeCurves(sqr)
        rs.ReverseCurve(xpldCrv[0])
        rs.ReverseCurve(xpldCrv[3])
        crvPoints = []
        for i in range(len(xpldCrv)):
            curve = xpldCrv[i]
            if i % 2 == 0:
                crvPoints.append(rs.DivideCurve(curve,x))
            else:
                crvPoints.append(rs.DivideCurve(curve,y))
            #divide up the curve into points based on x and y
            #add the resulting points to the curvePoints List. Each of the resulting points sets are a list themsleves
        for p1, p2 in zip(crvPoints[0], crvPoints[2]):
            #draw a line between p1, p2
            print(p1)
            #rs.AddLine(p1,p2)
            self.penUp()
            self.goto(p1[0],p1[1],p1[2])
            self.penDown()
            self.goto(p2[0],p2[1],p2[2])
        for p1, p2 in zip(crvPoints[1], crvPoints[3]):
            self.penUp()
            l = self.goto(p1[0],p1[1],p1[2])
            self.penDown()
            self.goto(p2[0],p2[1],p2[2])

    #
    def jump(self, force, dis):
    #make three points that together they can make an Arc, the first point would be heading position)
        distance=rs.VectorScale(self.direction,dis)
        startPoint= rs.PointCoordinates(self.point)
        endpoint= [startPoint[0] + distance.X , startPoint[1] + distance.Y, startPoint[2] + distance.Z]
        midpoint= [startPoint[0] + distance.X/2 , startPoint[1] + distance.Y/2, startPoint[2] + distance.Z/2]
        rotatevec= rs.VectorRotate(self.direction, 90, [0,0,1])
        heightvec=rs.VectorScale(rotatevec,force)
        midpoint1= rs.AddPoint(midpoint)
        forcepoint=rs.MoveObject(midpoint1,heightvec)
        # jumppath2=rs.AddCurve([startPoint, forcepoint, endpoint])
        dirVec = rs.VectorCreate(endpoint,startpoint)
        rs.MoveObject(self.point,dirVec)
        jumppath3=rs.AddInterpCurve([startPoint, forcepoint, endpoint])

    #
    def weave(self, firstcurve, secondcurve, pointcount):

        e = rs.CurveLength(firstcurve)
        f = rs.CurveLength(secondcurve)

        p1 = rs.DivideCurveEquidistant(firstcurve,e/pointcount,True,True)

        p2 = rs.DivideCurveEquidistant(secondcurve,f/pointcount,True,True)
        points = []
        for i in range(len(p1)):
            points.append(p1[i])
            points.append(p2[i])
        for p in points:
            self.goto(p[0],p[1],p[2])

    #
    def weaverandom(self, firstcurve, secondcurve, pointcount):
        e = rs.CurveLength(firstcurve)
        f = rs.CurveLength(secondcurve)

        p1 = rs.DivideCurveEquidistant(firstcurve,e/pointcount,True,True)

        p2 = rs.DivideCurveEquidistant(secondcurve,f/pointcount,True,True)
        points = []

        for i in range(len(p1)):
            a = random.randint(0,pointcount - 1)
            b = random.randint(0,pointcount - 1)
            points.append(p1[a])
            points.append(p2[b])
        for p in points:
            l = self.goto(p[0],p[1],p[2])
            clength = rs.CurveLength(l)
            if clength > e/2:
                rs.DeleteObject(l)

    #
    def Polygon(self,radius,sides,num,dist):
        self.num = num
        self.dist = dist
        self.radius = radius
        self.sides = sides
        theta = 360/self.sides
        pt01 = rs.AddPoint(self.radius,0,0)
        pts = []
        pts.append(pt01)
        self.origin = [0,0,0]
        degrees = theta
        for m in range(0,self.num):
            pt01 = rs.AddPoint(self.radius,0+(self.dist*m),0)
            pts.append(pt01)
            for x in range(1,self.sides):
                tempPt = pts[-1]
                newPt = rs.RotateObject(tempPt,self.origin,degrees,None,True)
                pts.append(newPt)
            pts.append(pt01)
            self.polygon = rs.AddPolyline(pts)

    #
    def jitter(self, x , y, step):
        initialPosition = rs.PointCoordinates(self.point)
        for i in range(step):
            xJitter = initialPosition[0] + rd.uniform(0 , x)
            yJitter = initialPosition[1] + rd.uniform(0 , y)
            self.goto(xJitter, yJitter)
        self.goto(initialPosition[0], initialPosition[1])

    #
    def curveJitter(self, x , y, step):
        initialPosition = rs.PointCoordinates(self.point)
        points = []
        degree = 3
        knots = step + degree - 1
        for i in range(step):
            xJitter = initialPosition[0] + rd.uniform(0,x)
            yJitter = initialPosition[1] + rd.uniform(0 , y)
            pt = rs.AddPoint([xJitter, yJitter, 0])
            points.append([xJitter, yJitter, 0])
            rs.DeleteObjects(pt)
        rs.AddCurve(points)

    #
    def deflect(self,deflectPoint):
        """
        Takes a Point as an input.
        Point creates a force field.
        The turtle deflects around the point
        """
        defPtPos=rs.PointCoordinates(deflectPoint)
        prevPos = rs.PointCoordinates(self.point)
        deflectVector1 = rs.VectorScale(rs.VectorCreate(prevPos, defPtPos),0.33)
        deflectVector2 = -deflectVector1
        deflectVector90_1 = rs.VectorScale(rs.VectorRotate(deflectVector1,90,[0,0,1]),0.33)
        deflectVector90_2 = -deflectVector90_1

        deflectVectorList = [deflectVector1,deflectVector2,deflectVector90_1,deflectVector90_2]

        forcePts =[]
        for i in deflectVectorList:
            newPt = rs.CopyObject(deflectPoint)
            rs.MoveObject(newPt,i)
            forcePts.append(newPt)

        gotoPt = rs.PointCoordinates(forcePts[0])

        self.goto(gotoPt[0],gotoPt[1])
        rs.AddArc3Pt(forcePts[0],forcePts[1],forcePts[2])
        rs.AddArc3Pt(forcePts[1],forcePts[0],forcePts[3])
        rs.DeleteObjects(forcePts)

    #
    def ellipse(self, xheight, yheight, placement = 'center', angle = 0):
        """xheight: the x dimension of the ellipse before rotation \n
        yheight: the y dimension of the ellipse before rotation \n
        placement: (optional) 'center' places ellipse centered around the turtle, 'edge' places ellipse to the side of the turtle \n
        angle: (optional) rotates ellipse around the turtle's"""
        centerPoint = rs.AddPoint(self.point)
        if placement == 'edge':
            centerPoint = rs.MoveObject(centerPoint, rs.VectorScale(rs.VectorCreate([1,0,0],[0,0,0]), xheight/2))
        newEllipse = rs.AddCircle(centerPoint, xheight/2)
        ScaleFactor = yheight/xheight
        rs.ScaleObject(newEllipse, self.point, [1,ScaleFactor,0])
        newEllipse = rs.RotateObject(newEllipse,self.point,angle)
        rs.DeleteObject(centerPoint)

    #
    def cube(self, l, w, h):
#        a = rs.AddPoint(self.point)
        p = rs.rs.PointCoordinates(self.point)
        a = rs.AddPoint(p)
        b = rs.CopyObject(a,[l,0,0])
        c = rs.CopyObject(a,[l,w,0])
        d = rs.CopyObject(a,[0,w,0])
        e = rs.CopyObject(a,[0,0,h])
        f = rs.CopyObject(a,[l,0,h])
        g = rs.CopyObject(a,[l,w,h])
        h = rs.CopyObject(a,[0,w,h])
        box = rs.AddBox([a,b,c,d,e,f,g,h])
        rs.DeleteObjects([a,b,c,d,e,f,g,h])

    #
    def cubecenter(self, m1, m2, m3):
#       a = rs.AddPoint(self.point)
        p = rs.GetPoint("Enter center point")
        a = rs.AddPoint(p)
        l = m1/2
        w = m2/2
        h = m3/2
        b = rs.CopyObject(a,[l,w,-h])
        c = rs.CopyObject(a,[l,-w,-h])
        d = rs.CopyObject(a,[-l,-w,-h])
        e = rs.CopyObject(a,[-l,w,-h])
        f = rs.CopyObject(a,[l,w,h])
        g = rs.CopyObject(a,[l,-w,h])
        h = rs.CopyObject(a,[-l,-w,h])
        j = rs.CopyObject(a,[-l,w,(m3/2)])
        box = rs.AddBox([b,c,d,e,f,g,h,j])
        rs.DeleteObjects([a,b,c,d,e,f,g,h])

    #
    def sphere(self, radius):
        p = rs.rs.PointCoordinates(self.point)
        a = rs.AddPoint(p)
        box = rs.AddSphere(a,radius)
        rs.DeleteObject(a)
    #
    def cylinder(self,r,h):
        p = rs.rs.PointCoordinates(self.point)
        cylinder = rs.AddCylinder(p,h,r)

    #
    def jumpSphere(self,magnitude):
        a = rs.PointCoordinates(self.point)
        p = rs.AddPoint(a)
        sphere = rs.AddSphere(p,4)
        # print self.direction
        prevPos = rs.PointCoordinates(self.point)
        for i in range(1,110):
            rs.MoveObject(sphere,(1,0,20 / i))
        for i in range(1,110):
            rs.MoveObject(sphere,(1,0,-1 * i / 40))

    #
    @classmethod
    def getColorList(cls):
        colorList = {
        "red" : [255,0,0],
        "blue" : [0,0,255],
        "green" : [0,255,0],
        "yellow" : [255,185,15],
        "white" : [248,248,255],
        "coral" : [255,127,80],
        "aqua" : [0,255,255],
        "orchid" : [218,112,214],
        "gray" : [166,166,166],
        }
        return colorList

    # method for read a file and return it's content as a string
    def readFile(self, path):
        file = open(path, "r")
        content = file.read()

        return content

    # this method interprets the file content
    # and returns the list of points id, points coordinate
    # and points connection respectively
    def cleanFile(self, f):
        rows = f.split('\n')
        del rows[0]

        points = []
        coordinates = []
        connection = []

        # extract the points id
        for i in range(0, len(rows)-1):
            tmp = ''
            for j in range(0, len(rows)-1):
                if rows[i][j] != ',':     #!= checks if the value of two operands are equal, if values are not equal than the condition becomes true.
                    tmp += rows[i][j]
                else:
                    rows[i] = rows[i].split(tmp + ',')[1]
                    break
            points.append(tmp)

        # extract the point coordinates
        for i in range(0, len(rows)-1):
            tmp = ''
            count = 0
            for j in range(0, len(rows)-1):
                if rows[i][j] == ',' and count == 1:
                    rows[i] = rows[i].split(tmp + ',')[1]
                    break
                elif rows[i][j] == ',' and count < 2:
                    tmp += rows[i][j]
                    count += 1
                elif rows[i][j] != ',':
                    tmp += rows[i][j]
                else:
                    rows[i] = rows[i].split(tmp + ',')[1]
                    break

            coordinates.append(tmp.split(','))

        # extract the point connection
        for i in range(0, len(rows)-1):
            connection.append(rows[i].split('"')[1]) #The [1] then indexes that list at position 1
        for i in range(0, len(connection)-1):
            connection[i] = connection[i].split(',')

        return points, coordinates, connection

    # Method for change the scale of points
    def changeScale(points, new_scale):
        for i in range(0, len(points)):
            points[i][0] *= new_scale
            points[i][1] *= new_scale

        return points

    # Method for change the coordinate of points
    def changeScale(points, new_x_axis, new_y_axis):
        for i in range(0, len(points)):
            points[i][0] += new_x_axis
            points[i][1] += new_y_axis

        return points
