"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 6, Exercise 6-3
by Allen Downey
    Code written by Mustafa Ali.
"""

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word:str) -> bool:
    """Returns True if word is a palindrome."""
    if len('word') <= 2:
        return True
    elif first(word) == last(word):
        return is_palindrome(middle(word))
    else:
        return False


if __name__ == '__main__':
    print(is_palindrome('allen'))
    print(is_palindrome('bob'))
    print(is_palindrome('otto'))
    print(is_palindrome('redivider'))