import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)
tim.speed("fastest")


def change_color():
    """Returns random color"""
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_colour = (r, g, b)
    return random_colour


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.circle(100)
        tim.color(change_color())
        current_head = tim.heading()
        tim.setheading(current_head + size_of_gap)


draw_spirograph(5)
my_screen = Screen()
my_screen.exitonclick()
