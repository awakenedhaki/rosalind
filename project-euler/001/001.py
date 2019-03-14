#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n: int) -> int:
    '''
    Calculate sum of multiples 3 or 5 below 1000.
    '''
    # sum is the sum of values multiples of 3 or 5
    sum: int = 0
    for i in range(n):
        if (i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum

if __name__ == '__main__':
    print(solution(1000))
