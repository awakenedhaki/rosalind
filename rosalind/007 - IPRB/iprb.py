# iprb.py

# author: awakenedhaki

# Run in command line: $python iprb.py file-path

import sys

from itertools import combinations
from typing import List, Dict, Tuple

def mendelInheritance(k: int, m: int, n: int) -> float:
    '''
    Probability of individual possessing dominant allele, with random parents
    Assume that any two organisms can mate.

    Write a Punnet Square for visualization.
    AA x AA, only one possibility
    AA x Aa, all outcomes have an A
    AA x aa, all outcomes have an A
    Aa x Aa, 3/4 of outcomes have an A
    Aa x aa, half of the outcomes have an A
    aa x aa, no outcomes has an A
    '''
    probs: Dict[Tuple[str, str], float] = {
        ('AA', 'AA'): 1.00,
        ('AA', 'Aa'): 1.00,
        ('AA', 'aa'): 1.00,
        ('Aa', 'Aa'): 0.75,
        ('Aa', 'aa'): 0.50,
        ('aa', 'aa'): 0.00
    }
    pool: List[str] = ['AA'] * k + ['Aa'] * m + ['aa'] * n
    matings: List[Tuple[str, str]] = list(combinations(pool, 2))
    # sum: the sum of probabilities
    sum: int = 0
    for mating in matings:
        sum += probs[mating]
    return round(sum / len(matings), 5)

if __name__ == '__main__':
    try:
        filename: str = sys.argv[1]
    except FileNotFoundError:
        print('Run in command line: $python iprb.py file-path')
    finally:
        with open(f'{filename}', 'r') as infile:
            contents = infile.read().split()
        k, m, n = map(int, contents)
        print(mendelInheritance(k, m, n))