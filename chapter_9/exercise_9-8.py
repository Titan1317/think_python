"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 9, Exercise 9-8
by Allen Downey
    Code written by Mustafa Ali.
"""


from is_palindrome import is_palindrome


if __name__ == '__main__':
    i = 100000
    while i < 1000000:
        number = str(i)
        number_1 = str(i + 1)
        number_2 = str(i + 2)
        number_3 = str(i + 3)
        if is_palindrome(number[-4:]) and is_palindrome(number_1[-5:]) and is_palindrome(number_2[1:-1]) and is_palindrome(number_3):
            print(number)
            print(number_1)
            print(number_2)
            print(number_3)
        i += 1