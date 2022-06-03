""" This module contains a code example related to Think Python, 2nd Edition,
Chapter 5, Exercise 5-5 by Allen Downey
    Code written by Mustafa Ali.
"""

import turtle


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)


if __name__ == '__main__':
    turtle.tracer(0, 0)
    bob = turtle.Turtle()
    length = 10
    n = 5
    draw(bob, length, n)
    turtle.update()
    turtle.mainloop()
