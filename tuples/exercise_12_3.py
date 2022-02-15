""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 12, Exercise 12-3
by Allen Downey
    Code written by Mustafa Ali.
"""


import exercise_12_2


def metathesis(word_1:str, word_2:str) -> bool:
    """ Checks if an anagram pair forms a metathesis pair """
    count = 0
    for letter_1, letter_2 in zip(word_1, word_2):
        if letter_1 != letter_2:
            count += 1
    if count == 2:
        return True
    return False

if __name__ == '__main__':
    file = 'words.txt'
    words_in_file = exercise_12_2.word_list(file)
    all_anagrams = exercise_12_2.anagrams(words_in_file)
    for anagram_set in all_anagrams.values():
        for i in range(len(anagram_set) - 1):
            word_1 = anagram_set[i]
            for j in range(i + 1, len(anagram_set)):
                word_2 = anagram_set[j]
                if metathesis(word_1, word_2):
                    print([word_1, word_2])   