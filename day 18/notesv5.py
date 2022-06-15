import turtle as t 
import random

frank = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random.color = (r, g, b)
    return random_color

directions = [0, 90, 100, 270]
frank.pensize(15)
frank.speed("fastest")

for _ in range(200):
    frank.color(random_color())
    frank.forward(30)
    frank.setheading(random.choice(directions))





    
