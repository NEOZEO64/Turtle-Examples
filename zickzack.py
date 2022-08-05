import turtle
import time

t = turtle.Pen()

t.speed(10)

x = 1
while x == 1: # loop which runs 4-times
    t.forward(100)
    t.left(89) # turns only 89 degrees, not 90!
