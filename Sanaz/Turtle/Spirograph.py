#(Drawing Python Turtle Spirograph: (Hypotrochoid))

# Hypotrochoid: 
# x = (R - r) * cos(angle) + d * cos((R - r) / r * angle)
# y = (R - r) * cos(angle) - d * cos((R - r) / r * angle)

# Hypocycloid: 
# x = (R - r) * cos(angle) + r * cos((R - r) / r * angle)
# y = (R - r) * sin(angle) - r * sin((R - r) / r * angle)

# Epitrochoid:
# x = (R + r) * cos(angle) - d * cos((R + r) / r * angle)
# y = (R + r) * sin(angle) - d * sin((R + r) / r * angle)

# Epicycloid: 
# x = (R + r) * cos(angle) - r * cos((R + r) / r * angle)
# y = (R + r) * sin(angle) - r * sin((R + r) / r * angle)


import turtle
import math


# screen setting 
screen = turtle.Screen()
screen.setup(600,600)
screen.title("Drawing Python Turtle Spirograph: (Hypotrochoid)")

#Perform a TurtleScreen update. To be used when tracer is turned off.
screen.tracer(0,0)

turtle.speed(0)

#Make the turtle invisible. It’s a good idea to do this while you’re in the middle of doing some complex drawing, because hiding the turtle speeds up the drawing observably.
turtle.hideturtle()

turtle.up()
turtle.pensize(4)


# create of turtles
t = turtle.Turtle()
t.up()
t.hideturtle()
t.speed(0)

t2 = turtle.Turtle()
t2.hideturtle()
t2.speed(0)
first = True
R=200 #
r=R/33 #
d = R/2.2*1.9 #

t3 = turtle.Turtle()
t3.color("blue")
t3.hideturtle()
t3.speed(0)
t3.pensize(1)
t3.up()
t3.seth(0) #Set the orientation of the turtle to to_angle
t3.goto(0,-R)
t3.down()
t3.circle(R,steps=300)


t2.up()
t2.pensize(1)
t2.color('green')
first = True

#functions

def draw_circle(x,y,angle):
    global first #This TurtleScreen method is available as a global function only under the name clearscreen
    turtle.clear()
    turtle.up()
    turtle.seth(0)
    turtle.goto(x,y-r)
    turtle.down()
    turtle.color('orange')
    turtle.circle(r,steps=300)
    turtle.up()
    turtle.goto(x,y)
    turtle.dot(5,'blue')
    turtle.down()
    turtle.seth(angle)
    turtle.color('purple')
    turtle.fd(d)
    turtle.dot(5,'red')
    t2.goto(turtle.xcor(),turtle.ycor()) # turtle.xcor(): Return the turtle’s x coordinate.
    if first:
        t2.down()
        first = False

# math.degrees(x)= Convert angle x from radians to degrees
# math.radian(x)= Convert angle x from degrees to radians
# math.pi= The mathematical constant π = 3.141592…, to available precision
# math.cos(x)= Return the cosine of x radians
# math.sin(x)= Return the sine of x radians
# dist = Compute distance between two coordinates

# Hypotrochoid: 
# x = (R - r) * cos(angle) + d * cos((R - r) / r * angle)
# y = (R - r) * cos(angle) - d * cos((R - r) / r * angle)

# Epitrochoid:
# x = (R + r) * cos(angle) - d * cos((R + r) / r * angle)
# y = (R + r) * sin(angle) - d * sin((R + r) / r * angle)

angle = 0
dist = r*angle*math.pi/180
Radian = dist/R
x = (R-r)*math.cos(Radian)+ d * math.cos((R - r) / r * Radian)
y = (R-r)*math.sin(Radian)- d * math.cos((R - r) / r * Radian)
draw_circle(x,y,angle+Radian*180/math.pi)
while True:
    angle -= 6
    dist = r*angle*math.pi/180
    Radian = dist/R
    x = (R-r)*math.cos(Radian)+ d * math.cos((R - r) / r * Radian)
    y = (R-r)*math.sin(Radian)- d * math.cos((R - r) / r * Radian)
    draw_circle(x,y,angle+Radian*180/math.pi)
    if angle % 360 == 0 and int(round(Radian*180/math.pi)) % 360 == 0:
        break
    turtle.update()
    
turtle.clear()
t3.clear()
turtle.update()



















