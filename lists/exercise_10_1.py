""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-1
by Allen Downey
    Code written by Mustafa Ali.
"""

def nested_sum(t:list) -> int:
    sum = 0
    for list in t:
        for element in list:
            sum += element
    return sum


if __name__ == '__main__':
    t = [[1, 2], [3], [4, 5, 6]]
    print(nested_sum(t))