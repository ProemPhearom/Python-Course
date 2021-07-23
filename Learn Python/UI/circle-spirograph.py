
# import pacckage
import turtle

# set bg color , pensize and speed 
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)

#Outer loop
for i in range (6):
    # nested loop in list
    for colours in ["red",
    "magenta", "blue", "cyan",
    "green", "yellow", "white"]:
            turtle.color(colours)
            turtle.circle(100)
            turtle.left(10)

# hide the turtle or invisible
turtle.hideturtle()
# tell the windows don't close 
#Auto after a run finished 
turtle.mainloop


