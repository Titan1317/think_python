""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-7
by Allen Downey
    Code written by Mustafa Ali.
"""

def has_duplicates(_list:list) -> bool:
    """ Takes a list and returns True if there is
         any element that appears more than once.
    """
    for i in range(len(_list) - 1):
        if _list[i] in _list[i+1:]:
            return True
    return False


if __name__ == '__main__':
    t = [1, 2, 2]
    print(has_duplicates(t))