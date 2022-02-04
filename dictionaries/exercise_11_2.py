"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 11, Exercise 11-2
by Allen Downey
    Code written by Mustafa Ali
"""


def invert_dict(d):
    inverse = dict()
    for key in d:
        i_key = d[key]  # Inverted key
        i_val = key     # Inverted Value
        inverse.setdefault(i_key, []).append(i_val)
    return inverse


if __name__ == '__main__':
    d = {'a' : 2, 'b': 4, 'c': 4, 'd':5}
    i = invert_dict(d)
    print(i)