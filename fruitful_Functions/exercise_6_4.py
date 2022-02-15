""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 6, Exercise 6-4
by Allen Downey
    Code written by Mustafa Ali.
"""


def is_power(a:float, b:float) -> bool:
    """ Returns True if 'a' is a power of 'b'"""
    if a == 1 or a == b:  # Special case b ** 0 == 1
        return True
    elif a % b == 0 and b != 1:
        return(is_power(a/b, b))


if __name__ == '__main__':
    print(is_power(1, 6))