# imports python-extensions
import turtle
import time


# gives you a pen to paint with
t = turtle.Pen()
#    ^ the "turle." means, that the command "turtle.Pen()" comes from the turtle-extension


# go 100 pixels forward with our pen
t.forward(100)


# rotate the pen 45 degrees left 
t.left(45)


# go forward again 200 pixels
t.forward(200)

t.backward(50) # then go backward 50 pixels


t.right(20)

t.forward(60)

time.sleep(3) # wait 3 seconds until the python-program ends