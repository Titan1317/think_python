"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 5, Exercise 5-2
by Allen Downey
    Code written by Mustafa Ali.
"""

from math import pow


def check_fermat(a:int, b:int, c:int, n:int) -> None:
    """A function that checks if fermats' theorem is upholded
    given the following arguments;
        'a' (an integer),
        'b' (an integer),
        'c' (an integer) and
        'n' (the exponent to which each integer is raised,
        'n' should be greater than 2).
    """
    a_n = pow(a, n)
    b_n = pow(b, n)
    c_n = pow(c, n)
    fermat = a_n + b_n == c_n
    if fermat and n > 2:
        print('Holy smokes, Fermat was wrong!')
    else:
        print('No, that doesn’t work.')

def input_fermat() -> None:
    """A function that prompts the user to enter some integers
        and calls check_fermat to check wether fermats' theorem
        is upheld for the given integers.
    """
    a = input("Enter an integer for 'a'\n")
    b = input("Enter an integer for 'b'\n")
    c = input("Enter an integer for 'c'\n")
    n = input("Enter an integer for 'n' that is greater than 2\n")
    check_fermat(int(a), int(b), int(c), int(n))


if __name__ == '__main__':
    input_fermat()
