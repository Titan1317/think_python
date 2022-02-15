prefixes = 'JKLMNOPQ'
suffix = 'ooz'


def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

def count(word, letter) -> int:
    result = 0
    index = find(word, letter, 0)
    while index != -1:
        result += 1
        index = find(word, letter, index + 1)
    return result

if __name__ == '__main__':
    word = 'babanab'
    print(count(word, 'b')) 