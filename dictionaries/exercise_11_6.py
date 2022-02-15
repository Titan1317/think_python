""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 11, Exercise 11-6
by Allen Downey
    Code written by Mustafa Ali
"""


if __name__ == '__main__':

    import pronounce

    d = pronounce.read_dictionary()
    for word in d:
        if len(word) == 5:
            word_1 = word[1:]
            word_2 = word[0] + word[2:]
            pronounce_1 = d.get(word)
            pronounce_2 = d.get(word_1)
            pronounce_3 = d.get(word_2)
            if (pronounce_2 and pronounce_3):
               if (pronounce_1 == pronounce_2 == pronounce_3):
                print(word, word_1, word_2)