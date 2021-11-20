import turtle
n=int(input())
a=int(input())
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
turtle.left(90)
turtle.forward(a)
for i in range (1, n):
    turtle.left(90)
    turtle.forward(a/(i*2))
    turtle.left(90)
    turtle.forward(a/(i*2))
    turtle.left(90)
    turtle.forward(a/(i*2))
    turtle.left(90)
    turtle.forward(a/(i*2))

turtle.exitonclick()

