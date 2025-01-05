from turtle import Turtle,Screen
import time
from SNAKES import snake
from SNAKES import segments
import random
from snakefood import food
food.penup()
food.goto(random.randint(0,300),random.randint(0,300))
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)



screen.listen()


game_is_on = True
while game_is_on:
    screen.onkeypress(key='w',fun=snake().snake_direction_up)
    screen.onkeypress(key='s',fun=snake().snake_direction_down)
    screen.onkeypress(key='a',fun=snake().snake_direction_left)
    screen.onkeypress(key='d',fun=snake().snake_direction_right)
    if food.distance(segments[0])<15:
        food.goto(random.randint(0,300),random.randint(0,300))
       
    time.sleep(0.05)
    screen.update()
    for seg in range(len(segments)-1,0,-1):
        
        x_coordinate = segments[seg-1].xcor()
        y_coordinate = segments[seg-1].ycor()
        segments[0].forward(10)
        segments[seg].goto(x_coordinate,y_coordinate)
   
        





























screen.exitonclick()
