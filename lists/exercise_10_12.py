""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-12
by Allen Downey
    Code written by Mustafa Ali.
"""

from exercise_10_9 import concatenate_words
from exercise_10_10 import in_bisect

def interlock(word_1:str, word_2:str, start_index:int, alternate_step:int) -> str:
    """ Takes alternating characters from each string and makes a new string.
        Two words “interlock” if taking alternating letters from 
        each forms a new word.
    """    
    result = []
    delimiter = ''
    n = min(len(word_1), len(word_2))
    for i in range(start_index, n, alternate_step):
        result.append(word_1[i])
        result.append(word_2[i])
    i_word = delimiter.join(result) # Interlocked word.
    return i_word


if __name__ == '__main__':

    file = 'words.txt'
    word_list = concatenate_words(file)
    start = 0
    step = 3
    for i in range(len(word_list) - 1):
        for j in range(i + 1, len(word_list)):
            word_1 = word_list[i]
            word_2 = word_list[j]
            if len(word_1) == len(word_2):
                # Interlocked word
                i_word = interlock(word_1, word_2, start, step)
                if in_bisect(i_word, word_list, 0, len(word_list) - 1):
                    print(word_1, word_2, i_word)