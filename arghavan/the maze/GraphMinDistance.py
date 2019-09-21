import math
import turtle


def getNeighbours(conn, vindex):
    nbrs = []
    cs = conn[vindex]
    for ci in range(0, len(cs)):
        if cs[ci] > 0:
            nbrs.append(ci)
    return nbrs


def findShortestPath(conn, pathlist, src, dst):
    nbrs = getNeighbours(conn, src)

    if len(nbrs) == 0:
        return []

    minlen = len(conn[0]) + 1
    selected_pl = []
    pathlistcopy = pathlist.copy()

    for ni in nbrs:
        if ni == dst:
            pathlistcopy.append(ni)
            return pathlistcopy
        else:
            if pathlistcopy.count(ni) > 0: #avoid loop
                continue
            else:
                pathlistcopy.append(ni) #start from the previous recongnized path
                pl = findShortestPath(conn, pathlistcopy, ni, dst)
                pathlistcopy.remove(ni)
                if len(pl) > 0 and len(pl) < minlen:
                    minlen = len(pl)
                    selected_pl = pl

    return selected_pl


def findLongestPath(conn, pathlist, src, dst):
    nbrs = getNeighbours(conn, src)

    if len(nbrs) == 0:
        return []

    maxlen = 0
    selected_pl = []
    pathlistcopy = pathlist.copy()

    for ni in nbrs:
        if ni == dst:
            pathlistcopy.append(ni)
            return pathlistcopy
        else:
            if pathlistcopy.count(ni) > 0:
                continue
            else:
                pathlistcopy.append(ni)
                pl = findLongestPath(conn, pathlistcopy, ni, dst)
                pathlistcopy.remove(ni)
                if len(pl) > maxlen:
                    maxlen = len(pl)
                    selected_pl = pl

    return selected_pl


class MyVertex:
    def __init__(self, index, info):
        self.index = index
        infos = info.split(',')
        self.name = infos[0].upper()
        self.x = int(infos[1])
        self.y = int(infos[2])
        self.connections = []
        for i in range(3, len(infos)):
            self.connections.append(infos[i].upper())


nameMap = dict()
vertices = []

min_x = 1000000
min_y = 1000000
max_x = -1000000
max_y = -1000000

with open('connections.txt', 'r') as conn_file:
    for row in conn_file:
        r = row.strip()
        if r == '':
            continue
        v = MyVertex(len(nameMap), r)
        vertices.append(v)
        nameMap[v.name] = v

        # find x,y range:
        if v.x < min_x:
            min_x = v.x
        if v.x > max_x:
            max_x = v.x
        if v.y < min_y:
            min_y = v.y
        if v.y > max_y:
            max_y = v.y

print('Loaded connections for ' + str(len(nameMap)) + ' vertices!')
connections = [[0 for x in range(len(nameMap))] for y in range(len(nameMap))]

for v in vertices:
    for cn in v.connections:
        v2 = nameMap[cn]

        connections[v.index][v2.index] = 1

scrn = turtle.Screen()  # Creates a playground for turtles

delta_x = max_x - min_x
delta_y = max_y - min_y
delta_max = max(delta_x, delta_y)
scrn_width = delta_max * 1.1
scrn_x = min_x - 0.05 * delta_max
scrn_y = min_y - 0.05 * delta_max
scrn.setworldcoordinates(scrn_x, scrn_y, scrn_x + scrn_width, scrn_y + scrn_width)

myTurtle = turtle.Turtle()  # Create a turtle, assign to myturtle
# speed up drawing
myTurtle.speed(0)
scrn.tracer(1, 1)
myTurtle.penup()
myTurtle.hideturtle()
myTurtle.shape("triangle")
myTurtle.shapesize(0.6, 0.6)

for vn in nameMap:
    v = nameMap[vn]
    myTurtle.goto(v.x, v.y)
    myTurtle.dot(5, 'red')
    myTurtle.write(v.name)
    for cn in v.connections:
        v2 = nameMap[cn]
        myTurtle.pendown()
        if connections[v.index][v2.index] != connections[v2.index][v.index]:
            myTurtle.goto((v2.x + v.x) / 2, (v2.y + v.y) / 2)
            h = 180 * math.atan2(v2.y - v.y, v2.x - v.x) / 3.14159265
            myTurtle.setheading(h)
            myTurtle.stamp()
        myTurtle.goto(v2.x, v2.y)
        myTurtle.penup()
        myTurtle.goto(v.x, v.y)

src = '1'
dst = '81'
myTurtle.speed(8)
srcV = nameMap[src]
dstV = nameMap[dst]
#path list
pl = list()
#start point
pl.append(srcV.index)
path = findShortestPath(connections, pl, srcV.index, dstV.index)

if len(path) > 1:
    print("Found shortest path from '" + src + "' to '" + dst + "' with lenght of " + str(len(path)) + " :")
    pathtext = str(srcV.name)#path to hol
    for i in range(1, len(path)):
        pathtext = pathtext + ' > ' + vertices[path[i]].name

    print("   " + pathtext)

    myTurtle.penup()
    myTurtle.color('blue')
    myTurtle.pensize(4)

    for vi in path:
        v = vertices[vi]
        myTurtle.goto(v.x, v.y)
        myTurtle.pendown()

path = findLongestPath(connections, pl, srcV.index, dstV.index)

if len(path) > 1:
    print("Found longest path from '" + src + "' to '" + dst + "' with lenght of " + str(len(path)) + " :")
    pathtext = str(srcV.name)
    for i in range(1, len(path)):
        pathtext = pathtext + ' > ' + vertices[path[i]].name

    print("   " + pathtext)

    myTurtle.penup()
    myTurtle.color('red')
    myTurtle.pensize(2)

    for vi in path:
        v = vertices[vi]
        myTurtle.goto(v.x, v.y)
        myTurtle.pendown()

scrn.mainloop()  # Wait for user to close window
