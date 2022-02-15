""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 6, Exercise 6-2
by Allen Downey
    Code written by Mustafa Ali.
"""

def ack(m:int, n:int) -> int:
    """ Evaluates the Ackermann function given two non-negative
    integers.
    """
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


# For values of 'm' > 4, runtime error due to maximum recursion depth reached.
# For values of 'n' > 3, runtime error due to maximum recursion depth reached.
if __name__ == '__main__':
    print(ack(4, 3))
