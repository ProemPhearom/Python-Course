# import the turtle module all
from turtle import *

import turtle

turtle.bgcolor("black")
# turtle.speed(10)
#return or set pencolor and fillcolor 
color ("red", "yellow")
begin_fill()


#check while statement // is true working
while True :
    # move or draw 
    forward(200)
    left(170)
    #check decision
    if abs(pos()) <1:
        break;
end_fill()
#using screen events
done