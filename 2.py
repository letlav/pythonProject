import turtle
n=int(input())
a=int(input())
for i in range (n):
    turtle.left(90)
    turtle.forward(a*2/(i+1)/2)
    turtle.left(90)
    turtle.forward(a*2/(i+1)/2)
    turtle.left(90)
    turtle.forward(a*2/(i+1)/2)
    turtle.left(90)
    turtle.forward(a*2/(i+1)/2)

turtle.exitonclick()

