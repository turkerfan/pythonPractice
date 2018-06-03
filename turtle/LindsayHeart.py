import turtle
t=turtle.Pen
def curvemove():
  for i in range(200):
    turtle.right(1)
    turtle.forward(1)

turtle.penup()
turtle.setx(0)
turtle.sety(-100)
turtle.pendown()
turtle.color('black','red')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curvemove()
turtle.left(120)
curvemove()
turtle.forward(111.65)
turtle.end_fill()
turtle.done()