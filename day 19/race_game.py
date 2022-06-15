from turtle import Turtle, Screen
import turtle
 

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?? Enter your color: ")
colors = ["red", "blue", "green", "yellow", "cyan", "gold"]
y_postions = [-70, -40. -10, 10, 30, 50]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_postions[turtle_index])


if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pncolor()
            if winning_color == user_bet:
                print(f"You win!! The{winning_color} turtle is the winner!")
            else:
                print(f"You lose!! The{winning_color} turtle is the winner!!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()