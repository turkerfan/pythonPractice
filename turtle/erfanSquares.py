import turtle

turtle.shape("turtle")
turtle.speed(50)
sideLength = 50
unitAngle=10
n_sqares=40
colors=["red","purple","blue","green"]


for i in range(n_sqares):
  for j in range(4):
    turtle.color(colors[i%len(colors)])
    turtle.forward(sideLength)
    turtle.right(90)
  turtle.right(unitAngle)
turtle.penup()
turtle.setx(-100)
turtle.sety(-100)
turtle.pendown()
turtle.done()