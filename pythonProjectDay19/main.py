from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(height=400, width=500)
y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "blue", "yellow", "green", "purple", "black"]

turtle_list = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    turtle_list.append(new_turtle)

user_bet = my_screen.textinput(title="Make Your Bet", prompt="which turtle will win the race")


is_race_on = True
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_color:
                print(f"you won {winning_color} turtle won the race")
            else:
                print(f"you lost {winning_color} turtle won the race")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


my_screen.exitonclick()

