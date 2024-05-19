from turtle import Screen, Turtle

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("SnaKe Game")

for i in range(3):
    box = Turtle()
    box.color("white")
    box.shape("square")
    box.goto(x=0-(i*20), y=0)






my_screen.exitonclick()