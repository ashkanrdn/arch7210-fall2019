import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import Rhino.RhinoMath as rm
import math
import random
from System.Drawing import Color
import RhinoTurtle3D as rt
import csv
import copy
reload(rt)
#fix class inside of a class

class draw_xy(rt.Turtle):

    # Definition of a class %%%%%%%%%%
    class PlanPoint:
        name = ''
        x = 0
        y = 0
        connections = []  # array

    # Dictionary %%%%%%%%%%

    def __init__(self,point_csv_file_dir,start_pos=(0,0),scale=1,):
        rt.Turtle.__init__(self)
        self.max_x = -2000
        self.min_x = 2000
        self.max_y = -2000
        self.min_y = 2000

        self.allpoints = {}  # dictionary
        self.dir_points = point_csv_file_dir
        self.read_csv_()

        self.start_pos = list(start_pos)
        self.scale =scale

    def read_csv_(self):
            with open(self.dir_points) as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[1] == 'X':  # Eliminating the first row (name, x , y, connections)
                        continue
                    p = draw_xy.PlanPoint()
                    p.name = row[0]  # Columns separation
                    p.x = float(row[1])
                    p.y = float(row[2])
                    p.connections = str.split(row[3], ',')
                    self.allpoints[p.name] = p  # Creation of all points

    def set_start_pos(self,start_pos):
        self.start_pos = list(start_pos)

    def set_scale(self,scale):
        self.scale = scale
    
    def start_draw(self):
        #print(self.window.window_width(),self.window.window_height())

        temp_point ={}
        for i in range(5):

            temp_point = copy.deepcopy(self.allpoints)
            for pn in temp_point:
                print pn
                p = temp_point[pn]
                p.x *= self.scale
                p.y *= self.scale
                p.x += self.start_pos[0]
                p.y += self.start_pos[1]

                #temp_point[pn] = p
                
        # Finding each points and their connections %%%%%%%%%%
        for pn in temp_point:  # Finding each points from dictionary
            p = temp_point[pn]
            # turtle draws dot for p
            self.goto(p.x, p.y)
            for c in p.connections:
                q = temp_point[c]
                # turtle draws line form p to q
                curves = rs.AddLine((p.x,p.y),(q.x, q.y))
        return curves
 

#==========CODE STARTS HERE====================

# Clear the board
rs.DeleteObjects(rs.AllObjects(select=True))

p = draw_xy("D:\Desktop\Sample Plan.csv",start_pos=(0,0),scale=1)
p.set_scale(1)
p.set_start_pos((0,0))
p.start_draw()
