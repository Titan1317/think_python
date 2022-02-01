""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-4
by Allen Downey
    Code written by Mustafa Ali.
"""

def chop(t:list) -> None:
    """ Takes a list, modifies it by removing the first and last
        elements, and returns None.
    """
    del t[0]
    del t[-1]
    return None


if __name__ == '__main__':
    t = [1, 2, 3, 4]
    chop(t)
    print(t)
