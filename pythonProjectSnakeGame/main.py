from turtle import Screen
from snake import Snake
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("SnaKe Game")
my_screen.tracer(0)

snake = Snake()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.right, "Right")
my_screen.onkey(snake.left, "Left")

is_game_on = True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()


my_screen.exitonclick()
