"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 7, Exercise 7-1
by Allen Downey
    Code written by Mustafa Ali.
"""
from math import sqrt


def mysqrt(a:int) -> float:
    """Uses Newtons' method to approximate the square root of the
         given number.
    """
    x = a / 2 
    while True:
        y = (x + a / x) / 2
        if abs(x - y) < 0.000000000000000001:
            break
        x = y
    return x


def test_square_root() -> None:
    """Prints a table that compares the return values of 
        mysqrt and the sqrt method from the math module,
        for values from 1 to 9"""
    print('a' + ' ' * 2, end = ' ')
    print('mysqrt(a)' + ' ' * 11, end = ' ')
    print('math.sqrt(a)' + ' ' * 8, end = ' ')
    print('diff')
    print('-' + ' ' * 2, end = ' ')
    print('---------' + ' ' * 11, end = ' ')
    print('------------' + ' ' * 8, end = ' ')
    print('----')
    for i in range(1,10):
        diff = abs(mysqrt(i) - sqrt(i))
        print(float(i), end = ' ')
        print(str(mysqrt(i)) + ' ' * (20 - len(str(mysqrt(i)))),
            end = ' ')
        print(str(sqrt(i)) + ' ' * (20  - len(str(sqrt(i)))),
             end = ' ')
        print(diff)

test_square_root()