from turtle import Turtle,Screen
import time
from SNAKES import snake

import random
from snakefood import Food
snake_body = snake()

food = Food().food
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
    screen.onkeypress(key='w',fun=snake_body.snake_direction_up)
    screen.onkeypress(key='s',fun=snake_body.snake_direction_down)
    screen.onkeypress(key='a',fun=snake_body.snake_direction_left)
    screen.onkeypress(key='d',fun=snake_body.snake_direction_right)
    if food.distance(snake_body.segments[0])<15:
        food.goto(random.randint(0,300),random.randint(0,300))
        
       
    time.sleep(0.05)
    screen.update()
    for seg in range(len(snake_body.segments)-1,0,-1):
        
        x_coordinate = snake_body.segments[seg-1].xcor()
        y_coordinate = snake_body.segments[seg-1].ycor()
        snake_body.segments[0].forward(10)
        snake_body.segments[seg].goto(x_coordinate,y_coordinate)
   
        





























screen.exitonclick()
