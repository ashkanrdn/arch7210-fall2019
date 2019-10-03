
###### Import tools ######
import turtle


# Window Setup
window = turtle.Screen()
window.title("Drawing a plan ")
turtle.bgcolor("green")
turtle.color("black")


# Turtle
elsa = turtle.Turtle()
turtle.Screen().bgcolor("orange")
elsa.color("black")
elsa.speed(1)
elsa.penup()

class PlanPoint: # Definition of a class
    name = ''
    x = 0
    y = 0
    connections = [] # array

allpoints = {} # dictionary

import csv
with open('Sample Plan.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if row[1] == 'X':  # Eliminating the first row (name, x , y, connections)
            continue
        p = PlanPoint()
        p.name = row[0]  # Columns separation
        p.x = float(row[1])
        p.y = float(row[2])
        p.connections = str.split(row[3], ',')
        allpoints[p.name] = p


for pn in allpoints: # Finding each points from dictionary
    p = allpoints[pn]
    # turtle draws dot for p
    elsa.goto(p.x, p.y)
    elsa.dot(5, "red")
    elsa.write(p.name)
    for c in p.connections:
        q = allpoints[c]
        # turtle draws line form p to q
        elsa.goto(p.x, p.y)
        elsa.pendown()
        elsa.goto(q.x, q.y)
        elsa.penup()
