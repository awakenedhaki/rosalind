# fib.py

# author: awakenedhaki

import sys

# Run in command-line with $python fib.py file-path

def rabbitPop(n: int, k: int, pop=1) -> int:
    '''
    Calculate rabbit pairs after n months, increasing at k pairs.
    '''
    if n == 1 or n == 2:
        return pop
    return rabbitPop(n-1, k) + (rabbitPop(n-2, k) * k)

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except (FileNotFoundError, IndexError):
        print('Run in command-line with $python fib.py file-path')
    else:
        with open(filename, 'r') as infile:
            n, k = map(int, infile.readline().split())
        print(rabbitPop(n, k))
