prefixes = 'JKLMNOPQ'
suffix = 'ooz'

# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(letter + 'u' + suffix)
#     else:
#         print(letter + suffix)

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

word = 'banana'
def count(word, letter) -> int:
    result = 0
    index = find(word, letter, 0)
    while index != -1:
        result += 1
        index = index = find(word, letter, index + 1)
    return result

print(count(suffix, 'b')) 