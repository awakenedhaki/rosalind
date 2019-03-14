# tribonacci.py

# author: awakenedhaki

from typing import List

def tribonacci(signature: List[int], n: int) -> List[int]:
    b = sum(signature)
    while True:
        a, b = signature.append(b), sum(signature[-3:])
        if n <= len(signature):
            break
    return signature[:n]
