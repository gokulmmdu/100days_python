from turtle import Turtle

positions = [(0,0),(-20,0),(-40,0)]

move_distance =  20

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
       self.all_segment = []
       self.create_snake()
       self.head = self.all_segment[0]

    def create_snake(self):
        for position in positions:
            self.add_segment(position)
            

    def add_segment(self,position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.all_segment.append(segment)


    def extend(self):
        self.add_segment(self.all_segment[-1].pos())




    def Up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)


    def Down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)


    def Right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)  


    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)      


    def move(self):
        for seg_num in range(len(self.all_segment) - 1 , 0, -1):

            new_x = self.all_segment[seg_num - 1].xcor()
            new_y = self.all_segment[seg_num - 1].ycor()
            self.all_segment[seg_num].goto(new_x,new_y)
        self.head.fd(move_distance)
       