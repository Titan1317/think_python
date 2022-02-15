""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 3, Exercise 3-2
by Allen Downey
    Code written by Mustafa Ali
"""

def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f , v):
    f(v)
    f(v)

def do_four(f , v):
    do_twice(f , v)
    do_twice(f , v)

# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't
if __name__ == '__main__':
    do_four(print_twice , 'spam')