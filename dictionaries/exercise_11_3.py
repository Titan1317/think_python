"""This module contains a code example related to
Think Python, 2nd Edition, Chapter 11, Exercise 11-3
by Allen Downey
    Code written by Mustafa Ali
"""


known = dict()

def A(m:int, n:int) -> int:
    if m == 0:
        return n + 1
    else:
        if n == 0:
            return A(m - 1, 1)
        else:
            if (m, n) in known:
                return known[(m, n)]
            else:
                known.setdefault((m, n), A(m - 1, A(m, n - 1)))
                return known[(m, n)]


if __name__ == '__main__':
    print(A(3,4))
    print(known)