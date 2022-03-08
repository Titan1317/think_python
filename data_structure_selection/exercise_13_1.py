""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 13, Exercise 13-1
by Allen Downey
    Code written by Mustafa Ali.
"""


from string import punctuation, whitespace

words_in_file = list()


def remove_punctuation(word:str) -> str:
    for letter in word:
        if letter in punctuation:
            word = word.replace(letter, '')
    return word

def read_file(file_name:str) -> list:
    fin = open(file_name)
    lines = fin.readlines()
    for line in lines:
        words = line.split(whitespace)
        for word in words:
            word = word.strip(punctuation + whitespace)
            plain_word = remove_punctuation(word)
            words_in_file.append(plain_word.lower())

if __name__ == '__main__':
    file_name = 'alice_in_wonderland.txt'
    read_file(file_name)
    print(words_in_file)