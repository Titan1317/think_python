""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-6
by Allen Downey
    Code written by Mustafa Ali.
"""

def is_anagram(word_1:str, word_2:str) -> bool:
    """ Takes two strings and returns True if they are
         anagrams.\n
        Two words are anagrams if you can rearrange the
         letters from one to spell the other.
    """
    if len(word_1) != len(word_2):
        return False
    sum_word_1 = 0
    sum_word_2 = 0
    for i in range(len(word_1)):
        sum_word_1 += ord(word_1[i])
        sum_word_2 += ord(word_2[i])
    return sum_word_1 == sum_word_2


if __name__ =='__main__':
    word_1 = 'abcdef'
    word_2 = 'dbacfe'
    print(is_anagram(word_1, word_2))