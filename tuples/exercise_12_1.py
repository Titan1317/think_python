""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 12, Exercise 12-1
by Allen Downey
    Code written by Mustafa Ali.
"""


def format_words(word_list:list) -> list:
    """ Traverses a list of words removing potentially
    unwanted characters.
    """
    stripped_words = list()
    for word in word_list:
        if word == '\\r\\n':    # skip CRLF line break control characters
            continue
        stripped_word = word.lower().strip(" ':;,.?!")
        stripped_words.append(stripped_word)
    return stripped_words

def readfile(file:str) -> list:
    """ Reads the given file line by line
    to build a list of all the words
    in the file.
    """
    words_in_file = list()
    fin = open(file)
    lines = fin.readlines()
    for line in lines:
        word_list = line.split()
        stripped_words = format_words(word_list)
        words_in_file.extend(stripped_words)
    return words_in_file

def histogram(word, histogram:dict) -> dict:
    """ Records the letters in a list of words
    along with their frequencies in a dictionary.
    """
    for letter in word:
        if letter not in histogram:
            histogram.setdefault(letter, 0)
        histogram[letter] += 1

def invert_histogram(histogram:dict) -> dict:
    """ Inverts a given histogram such that
    the keys represent the frequencies.
    This helps with sorting.
    """
    frequencies = dict()
    for key in histogram:
        frequencies.setdefault(histogram[key], []).append(key)
    return frequencies

def print_frequencies(_list:list) -> None:
    """ Prints the elements of each tuple
     in a list.
    """
    for frequency, characters in _list:
        print(frequency, characters)

def most_frequent(_string:str) -> None:
    """ Prints the letters that appear in 
        a given word in descending order
        of frequency.
    """
    histo = dict()
    histogram(_string, histo)
    frequencies = invert_histogram(histo)
    item_list = list(frequencies.items())
    item_list.sort(reverse = True) # Sort in descending order of frequency.
    print_frequencies(item_list)


if __name__ == '__main__':
    file = 'sample_text.txt'
    words_in_file = readfile(file)
    histo = dict()
    for word in words_in_file:
        histogram(word, histo)
    frequencies = invert_histogram(histo)
    item_list = list(frequencies.items())
    item_list.sort(reverse = True) # Sort in decreasing order of frequency.
    print(words_in_file)
    print_frequencies(item_list)