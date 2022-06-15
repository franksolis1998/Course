from turtle import Turtle, turtle, Screen 

frank = Turtle()
screen = Screen()

def move_forwards():
    frank.forward(10)



screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()