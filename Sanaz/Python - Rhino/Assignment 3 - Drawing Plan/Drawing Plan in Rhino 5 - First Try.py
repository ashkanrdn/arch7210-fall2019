#### Solution 4 - Practical ######==============================================


# Import tools %%%%%%%%%%
from pprint import pprint
import rhinoscriptsyntax as rs
import Rhino.RhinoMath as rm
import math
import Rhino.Geometry as rg

#==============================================================================#

    def read_csv_(self):
        with open(self.dir_points) as csvfile:
            results = []
            for row in csvfile:
                row = row.split(",")
                row = [col.strip() for col in row]
                if row[1] == 'X':  # Eliminating the first row (name, x , y, connections)
                    continue
                p = {}
                p["name"] = row[0]  # Columns separation
                p["x"] = float(row[1])
                p["y"] = float(row[2])
                print(row[3])
                p["connections"] = row[3].split('.')
                self.allpoints[row[0]] = p  # Creation of all points
                
            print results

#==============================================================================#

