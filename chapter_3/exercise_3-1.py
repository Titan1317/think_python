"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 3, Exercise 3-1
by Allen Downey
    Code written by Mustafa Ali.
"""


def right_justify(text:str) -> None:
    n = len(text)
    print(' ' * (70 - n) + text)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't
if __name__ == '__main__':
    right_justify('monty')