import math
from swampy.TurtleWorld import *



def square(t, length):

    for i in range(4):
        fd(t, length)
        lt(t)


def polyline(t, n, length, angle):

    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(t, n, length):

    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):

    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)


def circle(t, r):
    arc(t, r, 360)

if __name__ == '__main__':
    world = TurtleWorld()    

    bob = Turtle()
    bob.delay = 0.001

    # draw a circle centered on the origin
    radius = 100
    pu(bob)
    fd(bob, radius)
    lt(bob)
    pd(bob)
    circle(bob, radius)

    wait_for_user()
