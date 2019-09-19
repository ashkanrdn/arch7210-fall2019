from turtle import Turtle
import turtle
import math
import random
import RunnerFollowerTurtleBehavior

#Set max number of movements for the turtles
NumMovements = 100

#Set the screen boundaries 
screenWidth = 800
screenHeight = 800

#Setup the windowframe
window = turtle.Screen()
window.setup(screenWidth,screenHeight)

#Create the new turtle runner & explosions
rick = RunnerFollowerTurtleBehavior.TurtleRunner()
meeseeks = RunnerFollowerTurtleBehavior.TurtleExplosion()

#List to store the follwer turtles and their coordinates
followers = []
followerCoordinates = []

#Loop to create the amount of desirable follwer turtles
for x in range(5):
    morty = RunnerFollowerTurtleBehavior.TurtleFollower(random.uniform(-100,100), random.uniform(-100,100))
    followers.append(morty)

#Loop to execute the process of turtles followinf the runner
counter = 0 
while counter < NumMovements:
    if counter > len(followers):
        counter = 0
    elif counter < len(followers):
        rick.flee(followers[counter])
    #print(counter)
    
    #rick.run()
    rick.outOfBounds(window)
    for follower in followers:
        follower.follow(rick)
        followerCoordinates.append(follower.pos())
        distance = meeseeks.explode(rick, followerCoordinates)
        if distance == True:
            turtle.done()
    counter = counter + 1