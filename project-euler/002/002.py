#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sum_even_fibonacci(n: int) -> int:
    '''
    Sum all even numbers in fibonacci sequence to n terms
    '''
    a: int = 2
    b: int = 1
    # sum is sum of b when b is even
    sum: int = 0
    while b <= n:
        if b % 2 == 0:
            sum += b
        a, b = a + b, a
    return sum

if __name__ == '__main__':
    print(sum_even_fibonacci(4_000_000))
