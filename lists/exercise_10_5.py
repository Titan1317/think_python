""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-5
by Allen Downey
    Code written by Mustafa Ali.
"""

def is_sorted(t:list) -> bool:
    """ Takes a list as a parameter and returns True if
    the list is sorted in ascending order and False otherwise.
    """
    if len(t) <= 1:
        return True
    elif t[0] > t[1]:
        return False
    return is_sorted(t[1:])


if __name__ == '__main__':
    print(is_sorted([1, 2, 2]))
    print(is_sorted(['b', 'a']))