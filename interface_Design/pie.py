""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 4, Exercise 4-2
by Allen Downey
    Code written by Mustafa Ali.
"""

from mypolygon import polygon

import math
import turtle


def slice(turtle:object, length:int) -> None:
    """A function that draws a straight line and returns
    the turtle to it's original position.\n
    -Arguments:
        turtle: A turtle object.
        length: The length of the line in pixels.
    """
    turtle.pd()
    turtle.fd(length)
    turtle.pu()
    turtle.bk(length)


def pie(turtle:object, length:int, slices:int) -> None:
    """ A general function that draws the shapes from Exercise
    4-3.
    It uses the symmetric properties of the lengths and
    angles of Isoceles triangles to draw appropiately 
    large polygons for the given the number of slices.\n
    -Arguments:
        turtle: A turtle object.
        length: the length of the slices in pixels.
        slices: The number of slices.
    """
    angle = 360 / slices  # Angle between the two equal sides of the triangle.
    opposite_angle = (180 - angle) / 2  # Opposite angles of the triangle.
    radians = math.pi / 180 * angle     # Iscosceles angle in radians.
    base = math.sqrt((2 * length ** 2) - (2 * length ** 2 * math.cos(radians)))    #Cosine rule calculates the length of the sides of the polygon.
    polygon(turtle, slices, base)

    # Draw a line from the starting position to the center of the Polygon.
    turtle.lt(opposite_angle) 
    turtle.fd(length)

    # Look to the next leftmost vertex
    turtle.lt(180 - angle)
    for i in range (slices - 1):

        # Slice the pie clockwise.
        slice(turtle, length)
        turtle.rt(angle)

    # Return the turtle to the starting position.
    turtle.pu()
    turtle.fd(length)
    turtle.lt(180 - opposite_angle)
    turtle.pd()


if __name__ == '__main__':
    bob = turtle.Turtle()
    length = 100
    base = 2.5 * math.sqrt((2 * length ** 2) - (2 * length ** 2 * math.cos(math.pi / 180 * ( 360 / 5))))

    bob.pu()
    bob.bk(base)
    bob.pd()
    pie(bob, length, 5)

    bob.pu()
    bob.fd(base)
    bob.pd()
    pie(bob, length, 6)

    bob.pu()
    bob.fd(base)
    bob.pd()
    pie(bob, length, 7)
    bob.hideturtle()

    # wait for the user to close the window
    turtle.mainloop()