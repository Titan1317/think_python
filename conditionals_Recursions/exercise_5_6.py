"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 5, Exercise 5-6
by Allen Downey
    Code written by Mustafa Ali.
"""


import turtle


def koch_curve(t:object, length:float) -> None:
    """Draws a koch curve with the given length.\n
    -Arguments:
        t: A turtle object
        length: length of each line segment
    """
    if length <= 3:
        t.fd(length)
        return
    angle = 60
    koch_curve(t, length / 3)
    t.lt(angle)
    koch_curve(t, length / 3)
    t.rt(2 * angle)
    koch_curve(t, length / 3)
    t.lt(angle)
    koch_curve(t, length / 3)


def snow_flake(t:object, length:float) -> None:
    """ Uses the koch_curve to draw a shape resembling a snowflake
    """
    for i in range(6):
        koch_curve(t, length)
        t.lt(60)


if __name__ == '__main__':
    turtle.tracer(0, 0)
    bob = turtle.Turtle()
    length = 100
    bob.pu()
    bob.bk(length)
    bob.pd()
    snow_flake(bob ,length)
    turtle.update()
    turtle.mainloop()