#playing with turtle graphics

import turtle

#create window
loadwindow = turtle.Screen()
turtle.colormode(255)

#turn off draw mode
turtle.speed(0)

#create and run turle
for i in range(100):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
    b=i
    if b>51:
        b=51
        
    turtle.color(i, 2*i, 5*b)
   
# wait for user to end 
