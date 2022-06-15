from turtle import Turtle, Screen

frank = Turtle()
screen = Screen()

def move_forwards():
    frank.forward(10)

def move_backwards():
    frank.backward(10)

def move_left(): 
    new_heading = frank.heading() + 10
    frank.setheading(new_heading) 

def move_right():
    new_heading = frank.heading() - 10
    frank.setheading(new_heading)


def clear():
    frank.clear()
    frank.penup()
    frank.home()
    frank.pendown()




screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_left, "d")

screen.exitonclick()