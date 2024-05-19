from turtle import Screen, Turtle
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("SnaKe Game")
my_screen.tracer(0)

positions = [(0, 0), (-20, 0), (-40, 0)]
boxs = []

for position in positions:
    box = Turtle("square")
    box.color("white")
    box.penup()
    box.goto(position)
    boxs.append(box)


is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    for box_num in range(len(boxs)-1, 0, -1):
        next_x = boxs[box_num-1].xcor()
        next_y = boxs[box_num-1].ycor()
        boxs[box_num].goto(next_x, next_y)
    boxs[0].forward(20)
    boxs[0].left(90)
    time.sleep(1)












my_screen.exitonclick()