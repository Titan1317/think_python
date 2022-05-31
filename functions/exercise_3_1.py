""" This module contains a code example related to Think Python, 2nd Edition, 
Chapter 3, Exercise 3-1 by Allen Downey
    Code written by Mustafa Ali.
"""


def right_justify(text: str) -> None:
    n = len(text)
    print(' ' * (70 - n) + text)


if __name__ == '__main__':
    right_justify('monty')
