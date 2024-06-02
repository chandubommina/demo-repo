from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_pad = Paddle((-350, 0))
right_pad = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(fun=right_pad.up, key="Up")
screen.onkey(fun=right_pad.down, key="Down")
screen.onkey(fun=left_pad.up, key="w")
screen.onkey(fun=left_pad.down, key="s")

is_game_on = True
while is_game_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_pad) < 50 and ball.xcor() > 320 or ball.distance(left_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
