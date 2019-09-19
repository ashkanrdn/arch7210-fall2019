from turtle import Turtle
import turtle
import math
import random

NumMovements = 100
screenWidth = 500
screenHeight = 500

window = turtle.Screen()
window.setup(screenWidth,screenHeight)

#This class contains vector calculations not provided in native turtle library
class Vec2DExpansion(Turtle):

        #Calculate the angle between two coordinates / resturns the obtained angle
        def findAngle(self,positionA, positionB):
            '''
            positionA : x and y coordinates of a turtle
            positionB : x and y coordinates of a turtle
            '''
            dy = positionB[1] - positionA[1]
            dx = positionB[0] - positionA[0]
            if dx == 0:
                return 180.0
            else:
                return math.atan2(dy, dx) * 180.0 / math.pi

        #Calculate the distance between two points / retuns the obtained distance
        def pointDistance(self,positionA, positionB):
            '''
            positionA : x and y coordinates of a turtle
            positionB : x and y coordinates of a turtle
            '''
            dy = positionB[1] - positionA[1]
            dx = positionB[0] - positionA[0]
            distance = math.sqrt((dx)**2 + (dy)**2)
            return distance

#Create a turtle that has the ability to run around the canvas
class TurtleRunner(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()

    #Make the turtle run randomly around the canvas
    def run(self):
        self.setheading(random.uniform(0,360))
        self.forward(50)

    #If turtle reaches the edges of the established canvas make it turn around and return to the canvas / 90% effective
    def outOfBounds(self, screen):
        '''
        screen : 2D canvas where the turtle draw and roam around
        '''

        #Establishing the canvas boundaries
        leftBound = - screen.window_width() / 2
        rightBound = screen.window_width() / 2
        topBound = screen.window_height() / 2
        bottomBound = -screen.window_height() / 2

        turtleX = self.xcor()
        turtleY = self.ycor()
        location = self.pos()
        origin = turtle.Vec2D(0,0) 
        #When turtle reaches boundary based on its coordinates \ make it turn around and move forward back to the canvas
        if turtleX > rightBound or turtleX < leftBound and turtleY > topBound or turtleY < bottomBound:
            self.undo()
            angle = Vec2DExpansion().findAngle(location, origin)
            self.setheading(angle)
            self.forward(100)
    
    #Make the turtle run away from other turtles
    def flee(self, otherTurtles):
        '''
        otherTurtles: other turtles objects 
        '''
        positionA = self.pos()
        positionB = otherTurtles.pos()
        angle = Vec2DExpansion().findAngle(positionB, positionA)
        self.setheading(angle)
        self.forward(200)


#Create a turtle that has the ability to follow another turtle around the canvas
class TurtleFollower(Turtle):
    def __init__(self, x = 0, y = 0):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(x,y)


    #Make the turtle follow another turtle
    def follow(self, otherTurtle):
        ''' 
        otherTurtle : other turtle objects
        '''
        positionA = self.pos()
        positionB = otherTurtle.pos()

        #Calculate the angle from the two coordinates and make the turtle move forward
        angle = Vec2DExpansion().findAngle(positionA, positionB)
        self.setheading(angle)
        self.forward(50)

class TurtleExplosion(Turtle):
        
        def __init__(self):
            super().__init__()
            self.hideturtle()
            self.penup()

        #When the selected turtle is reached by the other following turtles 
        #it will generate an explosion around it and stop the program
        def explode(self,turtleToExplode, listOfCoordinates):
            '''
            turtleToExplode : the turtle you want to house the effect
            listOfCoordinates : provide the coordinates of all the follower turtles
            '''
            x,y = 0,0
            for coordinates in listOfCoordinates:
                #Sprint(Vec2DExpansion().pointDistance(turtleToExplode.pos(),coordinates))
                if Vec2DExpansion().pointDistance(turtleToExplode.pos(),coordinates) < 50:
                    self.hideturtle()
                    self.penup()
                    self.goto(x,y)
                    self.pendown()
                    self.speed(0)
                    for i in range(50):
                        self.pensize(1)
                        self.clear()
                        self.circle(10*i)
                        self.sety((10*i)*(-1))
                    return True
                else:
                    return False