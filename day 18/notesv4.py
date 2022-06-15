import turtle as t 
import random

frank = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        frank.forward(100)
        frank.right(angle)

for shape_side_n in range(3, 11):
    frank.color(random.choice(colors))
    draw_shape(shape_side_n)