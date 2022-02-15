""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 12, Exercise 12-4
by Allen Downey
    Code written by Mustafa Ali.
"""



words_in_file = {'' : 0, 'a' : 1, 'i': 1}
# Memo that caches all the reducible children of a word.
reducible = dict()
reducible[''] = [''] # Base Case

def find_children(word:str) -> list:
    """ Builds a list of all the children words of a given
    word.
    """
    length = len(word)
    children = list()
    for i in range(length):
        list_letters = list(word)
        del list_letters[i]
        delimiter  = ''
        child = delimiter.join(list_letters)
        if child in words_in_file:
            children.append(child)
    return children

def reduce(word:str) -> list:
    """ Builds a list of all the children words of a given
    word that are reducible as well.
    """
    if word in reducible:
        return reducible[word]
    reducible_children = list()
    children = find_children(word)
    for child in children:
        if reduce(child):
            reducible_children.append(child)
    reducible[word] = reducible_children
    return reducible_children
            

if __name__ == '__main__':
    file = 'words.txt'
    fin = open(file)
    lines = fin.readlines()
    for line in lines:
        word = line.strip()
        if ('a' in word) or ('i' in word):
            words_in_file.update([(word, len(word))])
    
    reducible_words = dict()
    for word in words_in_file:
        if reduce(word):
                reducible_words.setdefault(len(word), []).append(word)
    
    length, words = sorted(reducible_words.items(), reverse = True)[0]
    print(length, words)