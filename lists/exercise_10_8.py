""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-8
by Allen Downey
    Code written by Mustafa Ali.
"""

from exercise_10_7 import has_duplicates
from random import randint


def generate_brithdays() -> list:
    """ Generates a list of strings, where each string is a 
        random birthday date.
    """
    birthdays = []
    for i in range(23):
        month = randint(1, 12)
        if month % 2 != 0 or month == 8:
            day = randint(1, 31)
        elif month == 2:
            day = randint(1, 29)
        else:
            day = randint(1, 30)
        birthdays.append('{}.{}'.format(day,month))
    return birthdays


if __name__ == '__main__':
    samples = 100
    count = 0
    for i in range(samples):
        sample = generate_brithdays()
        if has_duplicates(sample):
            count += 1
    probability = 100 * count / samples 
    print(probability)