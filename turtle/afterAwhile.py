from turtle import Turtle,Screen
from itertools import cycle

t=Turtle()
t.shape("turtle")

ANGLE = 4

colors = ["red", "purple", "blue", "yellow", "green"]

def spiral(t, radius, color_names):
  colors = cycle(color_names)

  for _ in range (180 // ANGLE):
    t.color(next(colors))
    t.circle(radius)
    t.left(ANGLE)

t.speed("fastest")
spiral(t, 40, colors)

screen = Screen()
screen.exitonclick()
