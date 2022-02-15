""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 12, Exercise 12-2
by Allen Downey
    Code written by Mustafa Ali.
"""


from pprint import pprint


def word_list(file:str) -> list:
    """ Reads a file of words and builds a list of all
    the words.
    """
    fin = open(file)
    lines = fin.readlines()
    words_in_file = list()
    for line in lines:
        word = line.strip()
        words_in_file.append(word)
    return words_in_file

def key_word(word:str) -> str:
    """ Splits a word into its letters and returns a tuple
    of the letters sorted in ascending order.
    """
    letters = list(word)
    letters.sort()
    return tuple(letters)

def anagrams(word_list: list) -> dict:
    """ Builds a dictionary of all the anagrams that appear
    in a list of words.
    """
    dictionary = dict()
    result = dict()
    for word in word_list:
        key = key_word(word)
        dictionary.setdefault(key, []).append(word)
    for key in dictionary:
        if len(dictionary[key]) > 1:
            result.update([(key, dictionary[key])])            
    return result

def sort_anagrams(anagrams:dict) -> dict:
    """ Builds a dictionary of anagrams in descending oder
    of the length of anagram sets.
    """
    values = anagrams.values()
    lengths = dict()
    sort_lengths = dict()
    for value in values:
        key =  len(value)
        lengths.setdefault(key, value)
    sort_lengths.update(sorted(lengths.items(), reverse = True))
    return sort_lengths

def eight_letters(file:str) -> dict:
    """ Reads a file of words and builds a list of all
    the words that have 8 letters.
    """
    fin = open(file)
    lines = fin.readlines()
    word_list = list()
    for line in lines:
        word = line.strip()
        if len(word) == 8:
            word_list.append(word)
    return word_list     


if __name__ == '__main__':

    # Exercise 12-2.1
    file = 'words.txt'
    words_in_file = word_list(file)
    all_anagrams = anagrams(words_in_file)
    for key in all_anagrams:
        print(all_anagrams[key])
    print()

    # Exercise 12-2.2
    longest_anagrams = sort_anagrams(all_anagrams)
    pprint(longest_anagrams, sort_dicts = False)
    print()

    # Exercise 12-2.3
    words_in_file = eight_letters(file)
    eight_letter_anagrams = anagrams(words_in_file)
    bingo = sort_anagrams(eight_letter_anagrams)
    pprint(bingo, sort_dicts = False)