"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 9, Exercise 9-9
by Allen Downey
    Code written by Mustafa Ali.
"""
from is_palindrome import is_palindrome


def solve_puzzle(age:int) -> bool:
    age_mom = age
    age_son = 0
    counter = 0
    life_expectancy = 100 - age
    i = 0
    while life_expectancy:
        if counter == 8:
            return age_son
        age_son += 1
        age_mom += 1
        first_half = str(age_mom)
        second_half = str(age_son)
        if is_palindrome(first_half + second_half.zfill(2)):
            counter += 1
        life_expectancy -= 1
    return False
    


if __name__ == '__main__':
    for i in range(13,100):
        if solve_puzzle(i):
            print('Age of Mom: ' + str(i + solve_puzzle(i)) + ' Age of Son: ' + str(solve_puzzle(i)))


