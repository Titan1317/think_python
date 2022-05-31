""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 13, Exercise 13-1
by Allen Downey
    Code written by Mustafa Ali.
"""


from string import punctuation, whitespace
from random import choice

unwanted = punctuation + whitespace + '“”' + '‘’' + '—'
words_in_file = dict()
valid_words = dict()
valid_words['a'] = None
valid_words['i'] = None


def english_words(filename:str) -> dict:
    """ Makes a dictionary of all the words in the English language."""
    fin = open(filename)
    lines = fin.readlines()
    for line in lines:
        word = line.strip()
        valid_words[word] = None

def remove_punctuation(word:str) -> str:
    """ Removes all punctuation from a given word string."""
    global punctuation
    for letter in word:
        if letter in punctuation + '‘’':
            word = word.replace(letter, '')
    return word

def process_words(words:list) -> list:
    """ Removes any unwanted punctuation and returns the word in lowercase."""
    global unwanted
    result = []
    for word in words:
        word = word.strip(unwanted)
        plain_word = remove_punctuation(word)
        result.append(plain_word.lower())
    return result

def is_compound(word:str) -> str:
    """ Checks if a word is made up of two different words seperated with a symbol"""
    global unwanted
    for letter in word:
        if letter in unwanted :
            return True
    return False

def read_file(file_name:str) -> dict:
    """ Writes all the lines in a given file into a dictionary."""
    fin = open(file_name, encoding = 'utf8')
    lines_in_file = fin.readlines()
    return lines_in_file

def collect_words(lines:list) -> list:
    """ Splits lines into individual words and processes them."""
    accumulator = []
    for line in lines:
        words = line.split()
        stripped_words = process_words(words)
        for word in stripped_words:
            if is_compound(word):
                split_words = word.split('—')
                accumulator.extend(process_words(split_words))
            else:
                accumulator.append(word)
    return accumulator

def make_histogram(file_name:str) -> dict():
    lines_in_file = read_file(file_name)
    word_list = collect_words(lines_in_file)
    for word in word_list:        
        frequency = words_in_file.setdefault(word, 0)
        words_in_file[word] = frequency + 1

def invert_histogram(histogram:dict) -> dict:
    inverse = dict()
    for key, val in histogram.items():
        i_key = val
        inverse.setdefault(i_key, []).append(key)
    return inverse

def most_frequent(frequencies:dict) -> None:
    sorted_list = sorted(frequencies.items(), reverse= True)
    print('The 20 most frequent words in the file are:', end = '\n\n')
    for frequency, words in sorted_list[:20]: 
        print(words, frequency)
    print()

def filter_words(words:dict) -> None:
    print('The following words are either non-sensical, typos or completely valid:', end = '\n\n')
    for word in words_in_file:
        if word not in valid_words:
            print(word)

def random_word(histogram:dict) -> str:
    result = list()
    for word, frequency in histogram.items():
        result.extend(([word] * frequency))
    return choice(result)
        

if __name__ == '__main__':
    file_name = 'frankenstein.txt'
    file_name_2 = 'words.txt'
    english_words(file_name_2)
    make_histogram(file_name)

    # Print the number of distinct words used in the book
    print('Total number of unique words in the file: ', len(words_in_file), end = '\n\n')

    # Make a frequency mapping
    inverted_histogram = invert_histogram(words_in_file)
    most_frequent(inverted_histogram)
    filter_words(words_in_file)
    print()
    print(random_word(words_in_file))