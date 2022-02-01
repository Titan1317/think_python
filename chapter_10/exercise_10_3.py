""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-3
by Allen Downey
    Code written by Mustafa Ali.
"""

def middle(t:list) -> list:
    """ Takes a list and returns a new list that contains all
        but the first and last elements of the given list.
    """
    result = t[1: -1]
    return result


if __name__ == '__main__':
    t = [1, 2, 3, 4]
    print(middle(t))