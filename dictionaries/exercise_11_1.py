"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 11, Exercise 11-1
by Allen Downey
    Code written by Mustafa Ali
"""

from append_concatenate import append_words

import in_bisect
import time


def make_dict(file:str) -> dict:
    fin = open(file)
    line = fin.readline()
    word_dict = dict()
    for line in fin:
        word = line.strip()
        word_dict[word] = word_dict.get(word, 0)
    return word_dict


if __name__ == '__main__':
    file = 'words.txt'
    word = 'sass'
    test_cases = 100
    word_dict = make_dict(file)
    word_list = append_words(file)
    dic = 0
    lis = 0

    for word in word_list:

        # Measure time elapsed for dictionary lookup.
        start_1 = time.time()
        word in word_dict
        elapsed_1 = time.time() - start_1

        # Measure the elapsed time for list lookup.
        start_2 = time.time()
        in_bisect.in_bisect(word, word_list, 0, len(word_list) - 1)
        elapsed_2 = time.time() - start_2

        # Increment the appropriate counters
        if elapsed_1 < elapsed_2:
            dic += 1
        elif elapsed_1 == elapsed_2:
            lis += 1
            dic += 1
        else:
            dic += 1

    if dic > lis:
        print('Dictionary provides faster lookup')
    elif dic == lis:
        print('Both types provide lookup at same speed')
    else:
        print('List lookup is faster!')