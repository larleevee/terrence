
import math
import turtle

terrence = turtle.Turtle()
screen = turtle.Screen()
screen.setup(660,660)

#calc y pos of point on curve
def y_pos(k):
    return 13*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)
# a Twycross approved, sensibly long line ^

#calc x pos of point on curve
def x_pos(k):
    return 16*math.sin(k)**3

terrence.speed(0)
screen.bgcolor("ivory")

for k in range(100000): #sensible big number
    x = x_pos(k)*15
    y = y_pos(k)*15

    terrence.goto(x, y) #go to calc point
    terrence.color("purple")
    terrence.goto(0, 0) #return to origin

#terrence sleepy time
terrence.done()
