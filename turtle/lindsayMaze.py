import turtle

turtle.shape("turtle")
turtle.speed(200)
unitLength = 5
colors=["red","purple","blue","green"]
for i in range (100):
  turtle.right(90)
  turtle.color(colors[i % 4])
  turtle.forward(i*unitLength)
turtle.done()