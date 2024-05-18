from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


my_screen.listen()
my_screen.onkey(fun=move_forwards, key="w")
my_screen.onkey(fun=move_backwards, key="s")
my_screen.onkey(fun=turn_right, key="a")
my_screen.onkey(fun=turn_left, key="d")
my_screen.onkey(fun=clear, key="c")
my_screen.exitonclick()

