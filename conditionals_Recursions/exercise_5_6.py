""" This module contains a code example related to Think Python, 2nd Edition,
Chapter 5, Exercise 5-6 by Allen Downey
    Code written by Mustafa Ali.
"""


import turtle


def koch_curve(t: object, length: float, angle: int) -> None:
    """ Draws a koch curve with the given length.\n
    -Arguments:
        t: A turtle object
        length: length of each line segment
    """
    if length <= 3:
        t.fd(length)
        return None
    koch_curve(t, length / 3, angle)
    t.lt(angle)
    koch_curve(t, length / 3, angle)
    t.rt(2 * angle)
    koch_curve(t, length / 3, angle)
    t.lt(angle)
    koch_curve(t, length / 3, angle)


def snow_flake(t: object, length: float, angle: int) -> None:
    """ Uses the koch_curve to draw a shape resembling a snowflake
    """
    for i in range(6):
        koch_curve(t, length, angle)
        t.lt(60)


if __name__ == '__main__':
    turtle.tracer(0, 0)
    bob = turtle.Turtle()
    length = 200
    angle = 60
    bob.pu()
    bob.bk(length / 2)
    bob.pd()
    # koch_curve(bob, length, angle)
    snow_flake(bob, length, angle)
    turtle.update()
    turtle.mainloop()
