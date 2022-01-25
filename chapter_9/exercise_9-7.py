"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 9, Exercise 9-7
by Allen Downey
    Code written by Mustafa Ali.
"""


def check_triple_duplicates(slice:str) -> bool:
    counter = 0
    previous = slice[0]
    for letter in slice[1:]:
        if letter == previous:
            counter += 1
        previous = letter
    if counter == 3:
        return True
    return False

def solve_puzzle(word:str) -> bool:
    # Trivial case
    if len(word) < 6:
        return False
    i = 0
    while i <= len(word) - 6:
        slice = word[i:i+6]
        if check_triple_duplicates(slice):
            return True
        i += 1
    return False


if __name__ == '__main__':
    fin = open('words.txt')
    line = fin.readline()
    word = line.strip()
    valid_words = 0
    for word in fin:
        if solve_puzzle(word):
            valid_words += 1
            print(word)