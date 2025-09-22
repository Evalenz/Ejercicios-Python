import turtle

t = turtle.Turtle()

t.speed(3)

d = 10
for i in range(150):
    t.forward(d)
    t.right(20)
    d += 2
turtle.done()

