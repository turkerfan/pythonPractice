import turtle
turtle.shape("turtle")

def curvemove():
  for i in range(250):
    turtle.right(1)
    turtle.forward(1)
turtle.color('orange','yellow')
for i in range(5):

  turtle.begin_fill()
  turtle.left(30)
  turtle.forward(150)
  curvemove()

  turtle.forward(150)
  turtle.end_fill()

  turtle.penup()
  turtle.right(150)
  turtle.forward(170)

  turtle.pendown()
  turtle.dot(15,"red")

  turtle.penup()
  turtle.right(150)
  turtle.forward(270)

  turtle.pendown()
turtle.done()
