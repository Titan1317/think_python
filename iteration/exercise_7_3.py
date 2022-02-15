""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 7, Exercise 7-3
by Allen Downey
    Code written by Mustafa Ali.
"""


import math

def estimate_pi() -> float:
    """ Estimates the value of pi using Srinivasa Ramanujans' infinite
    series.
    """
    k = 0
    result  = 0
    while True:
        last_term = (2 * math.sqrt(2) / 9801) * (math.factorial(4 * k) * (1103 + 26390 * k)) / (math.factorial(k) ** 4 * 396 ** (4 * k))
        if last_term < 10 ** - 15:
            break
        result += last_term
        k += 1
    return 1 / result


if __name__ =='__main__':
    print(estimate_pi())
    print(math.pi)
