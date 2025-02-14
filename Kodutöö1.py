# kujund 4
import turtle
kulg = 200

turtle.pensize(2)
turtle.speed(3)

for _ in range(5):
    turtle.left(90) 
    turtle.forward(kulg/2)
    turtle.right(90)
    turtle.forward(kulg)
    turtle.right(90)
    turtle.forward(kulg)
    turtle.right(90)
    turtle.forward(kulg)
    turtle.right(90)
    turtle.forward(kulg/2)
    turtle.right(20)
turtle.hideturtle()
turtle.done()