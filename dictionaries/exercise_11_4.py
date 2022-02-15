""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 11, Exercise 11-4
by Allen Downey
    Code written by Mustafa Ali
"""


def has_duplicates(_list:list) -> bool:
    """ Takes a list and returns True if there is
    any element that appears more than once.
    """
    d = dict()
    for element in _list:
        if element in d:
            print(d)
            return True
        d[element] = d.get(element, 0) + 1
    print(d)
    return False


if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8, 8]
    x = has_duplicates(list)
    print(x)