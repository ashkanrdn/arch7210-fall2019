#ResidentEvil Umbrella
#Original Code from://
#https://www.geeksforgeeks.org/turtle-programming-python/

import turtle 

#Set pen and background colors
colors = ['red', 'white'] 
someone = turtle.Pen() 
turtle.bgcolor('black') 

#Adjust speed / the higher the number the faster the pen moves
someone.speed(1000)

#Start drawing the spiral / helix
for x in range(300): 
    someone.pencolor(colors[x%2]) 
    someone.width(x/100 + 1) 
    someone.forward(x) 
    someone.left(45) 