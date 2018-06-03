import turtle
colors=["red","blue","purple","green","orange","pink"]
t=turtle.Pen()
turtle.bgcolor("black")
for x in range(100):
  t.circle(x)
  t.left(91)
  t.pencolor(colors[x % len(colors)])
  t.width(x / 100 + 1)
  t.forward(x)
  t.left(59)
