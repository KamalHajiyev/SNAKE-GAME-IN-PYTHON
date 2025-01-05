from turtle import Turtle
starting_position = [(0,0),(-20,0),(-40,0)]
segments=[]
class snake:
    for position in starting_position:
        new_seqment = Turtle('square')
        new_seqment.color('white')
        new_seqment.penup()
        new_seqment.goto(position)
        segments.append(new_seqment)


    def snake_direction_up(self):
        segments[0].setheading(90)
    
    
    def snake_direction_down(self):
        segments[0].setheading(270)
    def snake_direction_left(self):
        segments[0].setheading(180)
    def snake_direction_right(self):
        segments[0].setheading(0)