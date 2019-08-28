# is_square.py

__author__ = "awakenedhaki"

from math import sqrt

def is_square(n: int) -> bool:
    if (n > 0 and sqrt(n).is_integer()) or (n == 0):
        return True
    return False
