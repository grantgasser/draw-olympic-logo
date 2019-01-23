import turtle
import time

#circle constants
NUM_CIRLCES = 5
RADIUS = 50

#colors
colors = ['blue', 'yellow', 'black', 'green', 'red']

#location constants
start_x = -150
start_y = 50
move_x = 65
move_y = RADIUS

#set speed, pensize, wait a second before drawing
turtle.speed(1)
turtle.pensize(3)
time.sleep(1)


#draw 5 circles
for x in range(NUM_CIRLCES):
    turtle.pencolor(colors[x])

    #to alternate, if iterator is odd, draw circle lower
    if(x % 2 == 1):
        turtle.penup()
        turtle.goto(start_x + (x * move_x), start_y-move_y)
        turtle.pendown()
        turtle.circle(RADIUS)

    else:
        turtle.penup()
        turtle.goto(start_x + (x * move_x), start_y)
        turtle.pendown()
        turtle.circle(RADIUS)
    

#take some time to appreciate beauty of drawing
time.sleep(5)