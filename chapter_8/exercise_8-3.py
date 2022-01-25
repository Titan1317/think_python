"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 8, Exercise 8-3
by Allen Downey
    Code written by Mustafa Ali.
"""

def is_palindrome(word:str) -> bool:
    return word == word[::-1]