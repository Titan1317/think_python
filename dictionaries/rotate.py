"""Think Python, 2nd Edition, Chapter 8, Exercise 8-5
by Allen Downey
    Code written by Mustafa Ali.
"""


def rotate_word(word:str, rotation:int) -> str:
    """Takes a string and an integer as parameters,
        and returns a new string that contains the letters from the 
        original string rotated by the given amount.
    """
    # Guarding from wrong input
    if not word.isalpha():
        print('Please enter a valid word.')
        return None
    result = ''
    for letter in word:
        upper_case = ord('A') <= ord(letter) <= ord('Z')
        lower_case = ord('a') <= ord(letter) <= ord('z')
        num_val = ord(letter) + rotation # Numerical value of the character after rotation.
        in_range_upper = ord('A') <= num_val <= ord('Z')
        in_range_lower = ord('a') <= num_val <= ord('z')
        if (upper_case and in_range_upper) or (lower_case and in_range_lower):
            result += chr(num_val)
        elif upper_case:
            if num_val > ord('Z'):
                offset = num_val - ord('Z')
                result += chr(ord('A') + offset - 1)
            else:
                offset = ord('A') - num_val
                result += chr(ord('Z') - offset + 1)
        # Lower case
        else:
            if num_val > ord('z'):
                offset = num_val - ord('z')
                result += chr(ord('a') + offset - 1)
            else :
                offset = ord('a') - num_val
                result += chr(ord('z') - offset + 1)
    return result


if __name__ == '__main__':
    word = 'IBM'
    rotation = -1
    print(rotate_word(word, rotation))
             
