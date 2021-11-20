import turtle
a=list(map(int, input().split()))
for i in range (10):
    turtle.circle(a[i])
s=max(a)
turtle.pencolor("red")
turtle.circle(s)
turtle.exitonclick()