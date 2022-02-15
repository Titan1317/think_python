"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-2
by Allen Downey
    Code written by Mustafa Ali.
"""


def cumsum(t:list) -> list:
    """ Takes a list of numbers and returns the cumulative
    sum.
    """
    result = []
    cum = 0
    for i in t:
        cum += i
        result.append(cum)
    return result

if __name__ == '__main__':
    t = [1, 2, 3]
    print(cumsum(t))