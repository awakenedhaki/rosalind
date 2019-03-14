# array_diff.py

# author: awakenedhaki

from typing import List

def array_diff(a: List[int], b: List[int]):
    '''
    Removes all values of a that are in b.
    '''
    for i in b:
        a = [j for j in a if j != i]
    return a
