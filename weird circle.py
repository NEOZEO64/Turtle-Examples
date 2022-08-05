import turtle

t = turtle.Pen()

l = 1
x = 0

while l == 1: # loop which runs infinite
    x += 1
    t.forward(x)
    t.left(x)