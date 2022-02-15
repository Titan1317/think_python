""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 5, Exercise 5-3
by Allen Downey
    Code written by Mustafa Ali.
"""

def is_triangle(a:int, b:int, c:int) -> None:
    """ Checks if the three given integers, 'a', 'b' and 'c'
    can form sides of a traingle.
    """
    check_1 = a + b == c
    check_2 = a + c == b
    check_3 = b + c == a
    if check_1 or check_2 or check_3:
        print('No')
    else:
        print('Yes')

def input_sides() -> None:
    """ Promts the user to enter three integers and checks wether
    the integers can form the sides of a triangle
    """
    side_1 = input('Enter an Integer\n')
    side_2 = input('Enter an Integer\n')
    side_3 = input('Enter an Integer\n')
    is_triangle(side_1, side_2, side_3)


if __name__ == '__main__':
        input_sides()