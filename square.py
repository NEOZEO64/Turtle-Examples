import turtle
import time

t = turtle.Pen()

'''
You could code like this:

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)

t.forward(100)
t.left(90)
'''

# Or – the better way
x = 0
while x<4: # loop which runs 4-times
    x += 1
    t.forward(100)
    t.left(90)


time.sleep(3)