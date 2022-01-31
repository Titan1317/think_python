""" This module contains a code example related to
Think Python, 2nd Edition, Chapter 10, Exercise 10-10
by Allen Downey
    Code written by Mustafa Ali.
"""


def in_bisect( _value:str, _list, _start:int , _end:int ) -> int:
    mid = ( _start + _end )  // 2
    if _start > _end:
        return None 
    else:
        if _value < _list[mid]:
            return in_bisect( _value, _list, _start, mid - 1 )
        elif _value > _list[mid]:
            return in_bisect( _value, _list,  mid + 1, _end )
        else:
            return mid

if __name__ == '__main__':
    from exercise_10_9 import concatenate_words
    
    file = 'words.txt'
    word_list = concatenate_words(file)
    end = len(word_list) - 1
    word = 'ass'
    index = in_bisect(word, word_list, 0 , end)
    if index:
        print(word_list[index])



