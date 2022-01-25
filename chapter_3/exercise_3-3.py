"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 3, Exercise 3-3
by Allen Downey
    Code written by Mustafa Ali
"""


def do_twice(f):
    f()
    f()

def do_four_times(f):
    do_twice(f)
    do_twice(f)

def print_border(x:str, y:str) -> None:
    """x is either '|' or '+' and y is either '  ' or ' -'.
    Prints  |         
    or
    Prints  + - - - -
    depending on the choices of x and y respectively.
    """
    print(x + y * 4, end = ' ')

def do_border_twice(x:str = '|', y:str = "  "):
    """x is either '|' or '+' and y is either '  ' or ' -'.
    Prints  '|         |         |' by default,
    or
    Prints  '+ - - - - + - - - - +'
    depending on the choices of f and s respectively.
    """
    print_border(x, y)
    print_border(x, y)

def do_border_four_times(x:str = "|", y:str = "  ") -> None:
    """x is either '|' or '+' and y is either '  ' or ' -'.
    Prints  '|         |         |         |         |' by default,
    or
    Prints  '+ - - - - + - - - - + - - - - + - - - - +'
    depending on the choices of f and s respectively."""
    do_border_twice( x, y)
    do_border_twice( x, y)
    print(end = x)
    print()

def print_row( ):
    do_border_four_times('+', ' -')
    do_four_times(do_border_four_times)

def print_grid():
    do_four_times(print_row)
    do_border_four_times('+', ' -')


# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't
if __name__ == '__main__':
    print_grid()