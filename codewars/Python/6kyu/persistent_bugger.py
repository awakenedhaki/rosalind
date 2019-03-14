# persistent_bugger.py

# author: awakenedhaki

import operator

from functools import reduce

def persistence(n: int) -> int:
    '''
    Returns multiplicative persistence
    '''
    # counts: number of times to get a single digit
    count: int = 0
    product: int = n
    while product >= 10:
        count += 1
        product = reduce(operator.mul, map(int, list(str(product))),1)
    return count
