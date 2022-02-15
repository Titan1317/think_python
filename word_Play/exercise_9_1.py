"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 9, Exercise 9-1
by Allen Downey
    Code written by Mustafa Ali.
"""


def has_no_e(word:str) -> bool:
    if not avoids(word, 'e'):
        return False
    return True

def uses_all(word:str, required:str) -> bool:
    return uses_only(required, word)


def avoids(word:str, letters:str) -> bool:
    for letter in word:
        if letter in letters:
            return False
    return True

def uses_only(word:str, letters:str) -> bool:
    for letter in word:
        if letter not in letters:
            return False
    return True

def is_abecedarian(word:str) -> bool:
    previous = word[0]   # variable used to store the order of the previous letter.
    for letter in word[1:]:
        if letter < previous:
            return False
        previous = letter
    return True


if __name__ == '__main__':
    fin = open('words.txt')
    line = fin.readline()
    word = line.strip()
    # letters = input('Enter a string of required characters.\n')
    valid_words = 0
    for word in fin:
        if is_abecedarian(word):
            valid_words += 1
            print(word)
    print(valid_words)


