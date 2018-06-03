from turtle import Turtle,Screen
from itertools import cycle

t=Turtle()
t.shape("turtle")

ANGLE = 1

colors = ["red", "red", "red", "white", "white", "white", "green", "green", "green"]

def spiral(t, radius, color_names):
  colors = cycle(color_names)

  for _ in range (180 // ANGLE):
    t.color(next(colors))
    t.circle(radius)
    t.left(ANGLE)

def line(t, radius, l,color_names):
  colors = cycle(color_names)

  for _ in range (l // ANGLE):
    t.color(next(colors))
    t.circle(radius)
    t.forward(ANGLE)


t.speed("fastest")
r=60

spiral(t, r, colors)
t.penup()
t.setx(0)
t.sety(-2*r)
t.pendown()
spiral(t, r, colors)
t.penup()
t.setx(0)
t.sety(-4*r)
t.pendown()


spiral(t, r, colors)
t.right(180)
t.penup()
t.setx(0)
t.sety(4*r)
t.pendown()
spiral(t, r, colors)

t.penup()
t.setx(0)
t.sety(2*r)
t.pendown()
spiral(t, r, colors)

t.penup()
t.setx(0)
t.sety(4*r)
t.pendown()
line(t,r,4*r,colors)

t.penup()
t.setx(0)
t.sety(-6*r)
t.pendown()
line(t,r,4*r,colors)

t.penup()
t.setx(5*r)
t.sety(-5*r)
t.pendown()
t.left(90)

line(t,r,10*r,colors)


screen = Screen()
screen.exitonclick()
