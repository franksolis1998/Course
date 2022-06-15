from multiprocessing.dummy import current_process
import turtle as t
import random 

frank = t.Turtle
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


frank.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap):
        frank.color(random_color())
        frank.circle(100)
        frank.setheading(frank.heading() + size_of_gap)

draw_spirograph(5)



screen = t.Screen()
screen.exitonclick():