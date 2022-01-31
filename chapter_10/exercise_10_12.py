""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-12
by Allen Downey
    Code written by Mustafa Ali.
"""

def interlock(word_1:str, word_2:str,start:int = 2, step:int = 3) -> str:    
    result = []
    delimiter = ''
    n = min(len(word_1), len(word_2))
    for i in range(start, n, step):
        result.append(word_1[i])
        result.append(word_2[i])
    i_word = delimiter.join(result) # Interlocked word.
    return i_word


if __name__ == '__main__':

    from exercise_10_9 import append_words
    from exercise_10_10 import in_bisect

    file = 'words.txt'
    word_list = append_words(file)
    word_index = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) == len(word_list[j]):
                i_word = interlock(word_list[i], word_list[j])
                if in_bisect(i_word, word_list, 0, len(word_list) - 1):
                    print(word_list[i], word_list[j], i_word)

        