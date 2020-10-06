'''Created by Aakasha01Agarwal'''


import turtle

t=turtle.Turtle()

def init():

    t.getscreen().bgcolor('black')
    t.color('white')
    t.speed(1)                    #Change the speed here
    t.setheading(90)


def branch(len, angle):
    if len > 10:
        t.forward(len)
        t.right(angle)
        branch(len-15, angle)
        t.left(2*angle)
        branch(len-15, angle)
        t.right(angle)
        t.back(len)

init()
branch(100, 30)   ##takes length and angle in that order

turtle.done()