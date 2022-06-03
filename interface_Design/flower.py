""" This module contains a code example related to Think Python, 2nd Edition,
Chapter 4, Exercise 4-3
by Allen Downey
    Code written by Mustafa Ali
"""

from mypolygon import arc

import turtle


def petal(turtle: object, radius: float, angle: float):
    """ Draws a petal shape from exercise 4-2.\n
    -Arguments:
        turtle: A turtle object.
        radius: The radius extended by the arc.
        angle: The angle extended by the arc.
    """
    for i in range(2):
        arc(turtle, radius, angle)
        turtle.lt(180 - angle)


def flower_1(turtle: object, size: float, petals: int) -> None:
    """ This function arranges non overlapping petals into a
    flower shape.\n
    -Arguments:
            turtle: A turtle object.
            size: The height of each petal in pixels.
            petals: The number of petals.
    """
    step_angle = 360 / petals
    for i in range(petals):
        petal(turtle, size, step_angle)
        turtle.lt(step_angle)


def flower_2(turtle: object, size: float, petals: int) -> None:
    """ This function rescales the petals such that they overlap,
    resembling the shape of a flower.\n
    -Arguments:
            turtle: A turtle object.
            size: The height of each petal in pixels.
            petals: The number of petals.
    """
    step_angle = 360 / (petals / 2)  # The width of the petals increase.
    for i in range(petals):
        petal(turtle, size, step_angle)
        turtle.lt(step_angle - step_angle / 2)


if __name__ == '__main__':
    bob = turtle.Turtle()
    length = 120
    base = 2.5 * length

    bob.pu()
    bob.bk(base)
    bob.pd()
    flower_1(bob, 1.5 * length, 7)

    bob.pu()
    bob.fd(base)
    bob.pd()
    flower_2(bob, length, 10)

    bob.pu()
    bob.fd(base)
    bob.pd()
    flower_1(bob, 3.5 * length, 20)
    bob.hideturtle()

    # wait for the user to close the window
    turtle.mainloop()
