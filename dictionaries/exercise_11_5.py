"""Think Python, 2nd Edition, Chapter 11, Exercise 11-5
by Allen Downey
    Code written by Mustafa Ali.
"""


from rotate import rotate_word

import exercise_11_1

if __name__ == '__main__':
    file = 'words.txt'
    word_dict = exercise_11_1.make_dict(file)
    for word in word_dict:
        for i in range(1, 26):
            reversed = rotate_word(word, i)
            if reversed in word_dict:
                print(word, reversed)