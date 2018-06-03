from turtle import Turtle

t=Turtle()
t.shape("arrow")
t.screen.bgcolor("black")
colors=["red","yellow","purple","blue","deep pink","green"]
t.screen.tracer(0,0)

for x in range(100):
  t.circle(x)
  t.color(colors[x%6])
  t.left(60)

t.screen.exitonclick()
t.screen.mainloop()