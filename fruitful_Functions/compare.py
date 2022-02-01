from math import pow, sqrt


def compare(x, y) -> int:
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1


def hypotenuse(a:float, b:float) -> float:
    return sqrt(pow(a, 2) + pow(b, 2))


def is_between(x:float, y:float, z:float) -> bool:
    return x <= y <= z

if __name__ == '__main__':
   print(is_between(1,5,3))