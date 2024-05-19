from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.boxs = []
        self.create_snake()
        self.head = self.boxs[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_box(position)

    def add_box(self, position):
        box = Turtle("square")
        box.color("white")
        box.penup()
        box.goto(position)
        self.boxs.append(box)

    def extend(self):
        self.add_box(self.boxs[-1].position())

    def move(self):
        for box_num in range(len(self.boxs)-1, 0, -1):
            next_x = self.boxs[box_num-1].xcor()
            next_y = self.boxs[box_num-1].ycor()
            self.boxs[box_num].goto(next_x, next_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

