""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 6, Exercise 6-5
by Allen Downey
    Code written by Mustafa Ali.
"""


def gcd(a:float, b:float) -> float:
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)

if __name__ == '__main__':
    print(gcd(43, 34))