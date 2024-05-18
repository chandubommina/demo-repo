from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(90)

def turn_right():
    tim.right(90)

def clear_screen():
    my_screen.clearscreen()


my_screen.listen()
my_screen.onkey(fun=move_forwards, key="w")
my_screen.onkey(fun=move_backwards, key="s")
my_screen.onkey(fun=turn_right, key="a")
my_screen.onkey(fun=turn_left, key="d")
my_screen.onkey(fun=clear_screen, key="c")
my_screen.exitonclick()

