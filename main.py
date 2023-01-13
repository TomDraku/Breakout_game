from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from box import Box
from scoreboard import Scoreboard
import time
import random



width = [4,5]
random_width = random.choice(width)


colors = ["Blue","Green", "Yellow","Orange","Red"]


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

mypaddle = Paddle((0,-250))
myball = Ball()
scoreboard = Scoreboard()





boxes = []  # define an empty list to store the boxes
numbers_x = [-470,-485]
y = 30
for color in colors:
    x = random.choice(numbers_x)
    y = y+25
    positions = (x,y)
    for i in range(14):
        x = x+85
        
        box = Box((x, y), color=color)
        boxes.append(box) # append the box to the list
       

        
        
        
        

screen.listen()
screen.onkey(mypaddle.go_right, "Right")
screen.onkey(mypaddle.go_left, "Left")

game_status = 3
game_is_on = True




while game_is_on == True:
    time.sleep(0.01)
    screen.update()
    
    
    myball.move()
    
    #Detect collision with wall
    if myball.ycor()>285:
        myball.bounce_y()
    elif myball.xcor()>385:  
        myball.bounce_x()
    elif myball.xcor() < -385:
        myball.bounce_x()
        
    #Detect collision with paddle
    if myball.distance(mypaddle) < 50 and myball.ycor()<-235:
        myball.bounce_y()
        
        
    #Detect collision with box
    for box in boxes:
        if  myball.distance(box) < 40:
            myball.bounce_y()
            box.goto(-600, 0)
            scoreboard.point()
        
    
        
    #Detect  paddle misses:
    if myball.ycor() < -305:
        myball.reset_position()
        game_status -= 1
        if game_status == 0:
            game_is_on = False
            scoreboard.game_over()
        print(game_status)
            
    





screen.exitonclick()