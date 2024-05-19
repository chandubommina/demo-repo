from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.boxs = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            box = Turtle("square")
            box.color("white")
            box.penup()
            box.goto(position)
            self.boxs.append(box)

    def move(self):
        for box_num in range(len(self.boxs)-1, 0, -1):
            next_x = self.boxs[box_num-1].xcor()
            next_y = self.boxs[box_num-1].ycor()
            self.boxs[box_num].goto(next_x, next_y)
        self.boxs[0].forward(MOVE_DISTANCE)

    def up(self):
        self.boxs[0].setheading(90)

    def down(self):
        self.boxs[0].setheading(270)

    def right(self):
        self.boxs[0].setheading(0)

    def left(self):
        self.boxs[0].setheading(180)

