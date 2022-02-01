""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-11
by Allen Downey
    Code written by Mustafa Ali.
"""

if __name__ == '__main__':
    from exercise_10_10 import in_bisect
    from exercise_10_9 import concatenate_words


    file = 'words.txt'
    word_list = concatenate_words(file)
    end = len(word_list) - 1
    for word in word_list:
        reverse = word[::-1]
        index = in_bisect(reverse, word_list, 0, end)
        if index:
            print(word, word_list[index])
