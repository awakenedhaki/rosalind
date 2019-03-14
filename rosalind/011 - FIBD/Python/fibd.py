# fibd.py

# awakenedhaki

# Run in command-line: python script-path file-path

import sys

def rabbitPop(n: int, k: int, pop=1) -> int:
    if n == 1 or n == 2:
        return pop
    return rabbitPop(n-1, k) + (rabbitPop(n-2, k) * k)