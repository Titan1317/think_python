""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-9
by Allen Downey
    Code written by Mustafa Ali.
"""

import time


def append_words( file:str) -> list:
    """ Reads the file words.txt and builds a list with one element per
    word using the append method.
    """
    fin = open(file) 
    line = fin.readline()
    word_list = []
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def concatenate_words(file:str) -> list:
    """Reads the file words.txt and builds a list with one element per
    word using concatenation."""
    fin = open(file) 
    line = fin.readline()
    word_list = []
    for line in fin:
        word = line.strip()
        word_list += [word]
    return word_list


if __name__ == '__main__':
    file = 'words.txt'
    append = 0
    concatenate = 0
    for i in range(100):
        # Measure elapsed time for append_words.
        start_1 = time.time()
        t_1 = append_words(file)
        elapsed_time_1 = time.time() - start_1

        # Measure the elapsed time for concatenate_words.
        start_2 = time.time()
        t_2 = concatenate_words(file)
        elapsed_time_2 = time.time() - start_2

        if elapsed_time_1 < elapsed_time_2:
            append += 1
        elif elapsed_time_1 == elapsed_time_2:
            append += 1
            concatenate += 1
        else:
            concatenate += 1

    if append > concatenate:
        print('append_words is faster.')
    elif append == concatenate:
        print('append_words and concatenate_words are just as fast.')
    else:
        print('concatenate_words is faster!')