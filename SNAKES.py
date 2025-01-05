from turtle import Turtle
starting_position = [(0,0),(-20,0),(-40,0)]

class snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        

    def create_snake(self):
        for position in starting_position:
            new_seqment = Turtle('square')
            new_seqment.color('white')
            new_seqment.penup()
            new_seqment.goto(position)
            self.segments.append(new_seqment)
    def extend(self):
        new_tail = Turtle('square')
        new_tail.color('white')
        new_tail.penup()
        new_tail.goto(self.segments[-1].position())
        self.segments.append(new_tail)


    def snake_direction_up(self):
        self.segments[0].setheading(90)
    
    
    def snake_direction_down(self):
        self.segments[0].setheading(270)
    def snake_direction_left(self):
        self.segments[0].setheading(180)
    def snake_direction_right(self):
        self.segments[0].setheading(0)

    