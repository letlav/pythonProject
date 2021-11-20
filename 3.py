import turtle
import random
a=int(input())
n=int(input())
'''colormode(255)
turtle.pencolor(random.randint(0, 255))'''
'''def f(a):'''
for i in range (n):
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(a)
    turtle.right(120)
    turtle.forward(a)
    turtle.left(60)
    turtle.forward(a)
    turtle.left(120)
'''print(f(a))'''
turtle.exitonclick()

