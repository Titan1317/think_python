""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-9
by Allen Downey
    Code written by Mustafa Ali.
"""

import time


def append_words( file:str) -> None:
    fin = open(file) 
    line = fin.readline()
    word_list = []
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list

def concatenate_words(file:str) -> list:
    fin = open(file) 
    line = fin.readline()
    word_list = []
    for line in fin:
        word = line.strip()
        word_list += [word]
    return word_list


if __name__ == '__main__':
    file = 'words.txt'

    # Measure elapsed time for append_words.
    start_1 = time.time()
    t_1 = append_words(file)
    elapsed_time_1 = time.time() - start_1
    print(t_1[:10])
    print(elapsed_time_1)

    # Measure the elapsed time for concatenate_words.
    start_2 = time.time()
    t_2 = concatenate_words(file)
    elapsed_time_2 = time.time() - start_2
    print(t_2[:10])
    print(elapsed_time_2)

    # Measure the absolute difference.
    difference = abs(elapsed_time_1 - elapsed_time_2)

    if elapsed_time_1 < elapsed_time_2:
        print('The append method is faster by {}'.format(difference))
    else:
        print('Concatenation is faster by {}'.format(difference))