""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 4, Exercise 4-5
by Allen Downey
    Code written by Mustafa Ali.
"""

from mypolygon import arc

import turtle


def archimedian_spiral(turtle:object, angle:float):
    """ Draws an  archimedian_spiral with the given angle.
    t: Turtle
    angle: degrees rotated
    """
    for i in range(angle):
        a = 0.25    
        radius = a * i  # The radius of the arc drawn in the current iteration.
        arc(turtle, radius, 1)
        turtle.hideturtle()

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.
if __name__ == '__main__':
    bob = turtle.Turtle()
    turtle.tracer(0, 0)

    # draw a spiral centered on the origin
    radius = 50
    archimedian_spiral(bob, 2 * 720)

    turtle.update()
    # wait for the user to close the window
    turtle.mainloop()