import math

def square_root(n):
    if n < 0:
        raise ValueError("Can not compute square root of a negative number")
    return math.sqrt(n)