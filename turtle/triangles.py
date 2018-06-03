import turtle

turtle.shape("turtle")
turtle.speed(100)
sideLength = 60
unitAngle=10
n_tri=300
colors=["red","blue","green"]


for i in range(n_tri):
  for j in range(3):
    turtle.color(colors[i%len(colors)])
    turtle.forward(i+sideLength)
    turtle.right(120)
  turtle.right(unitAngle)
  turtle.penup()
  turtle.left(60)
  turtle.forward(5)
  turtle.right(60)
  turtle.pendown()

turtle.penup()
turtle.setx(-100)
turtle.sety(-100)
turtle.pendown()
turtle.done()