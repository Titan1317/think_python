""" This module contains a code example related to Think Python, 2nd Edition,
Chapter 3, Exercise 3-3 by Allen Downey
    Code written by Mustafa Ali
"""


def do_twice(f, x, y):
    f(x, y)
    f(x, y)


def do_four_times(f, x, y):
    do_twice(f, x, y)
    do_twice(f, x, y)


def print_border(x: str, y: str) -> None:
    """ x is either '|' or '+' and y is either '  ' or ' -'.
    Prints | or prints  + - - - - depending on the choices of x
    and y respectively.
    """
    print(x + y * 4, end=' ')


def print_border_twice(x: str, y: str) -> None:
    """ x is either '|' or '+' and y is either '  ' or ' -'.
    Prints ||| by default, or Prints + - - - - + - - - - +
    depending on the choices of f and s respectively.
    """
    do_twice(print_border, x, y)
    print(end=x)
    print()


def print_border_four_times(x: str, y: str) -> None:
    """ x is either '|' or '+' and y is either '  ' or ' -'.
    Prints ||||| by default, or 
    Prints + - - - - + - - - - + - - - - + - - - - + depending
    on the choices of f and s respectively.
    """
    do_four_times(print_border, x, y)
    print(end=x)
    print()


def print_row_1(x: str, y: str) -> None:
    print_border_twice(x, y)
    do_four_times(print_border_twice, '|', '  ')


def print_row_2(x: str, y: str) -> None:
    print_border_four_times(x, y)
    do_four_times(print_border_four_times, '|', '  ')


def print_grid_1(x: str, y: str) -> None:
    do_twice(print_row_1, x, y)
    print_border_twice(x, y)


def print_grid_2(x: str, y: str) -> None:
    do_four_times(print_row_2, x, y)
    print_border_four_times(x, y)


if __name__ == '__main__':
    print_grid_1('+', ' -')
    print()
    print_grid_2('+', ' -')
