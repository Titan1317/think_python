"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 9, Exercise 9-8
by Allen Downey
    Code written by Mustafa Ali.
"""


from is_palindrome import is_palindrome

def has_duplicates(word:str) -> bool:
    i = 0
    while i < len(word) - 1:
        if word[i] in word[i+1:]:
            return True
        i += 1
    return False
        


def solve_puzzle(number:str) -> bool:
    first_half = number[:3]
    second_half = number[3:]
    if has_duplicates(first_half) or has_duplicates(second_half):
        return True
    for digit in first_half:
        if digit in second_half:
            start = number.index(digit) 
            end = number.index(digit,3)
            difference =abs(start - end)
            if difference > 2:
                return is_palindrome(number[start + 1: end])
            return True
    return False

if __name__ == '__main__':
    i = 300000
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