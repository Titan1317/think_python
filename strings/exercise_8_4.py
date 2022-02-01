"""Think Python, 2nd Edition, Chapter 8, Exercise 8-4
by Allen Downey
    Code written by Mustafa Ali.
"""
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


if __name__ == '__main__':
    s = 'aSS'
    print(any_lowercase1(s))
    print(any_lowercase2(s))
    print(any_lowercase3(s))
    print(any_lowercase4(s))
    print(any_lowercase5(s))