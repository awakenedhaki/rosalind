# vowel_count.py

# author: awakenedhaki

from typing import List

def getCount(inputStr: str) -> int:
    '''
    Counts number of vowels in a string.
    '''
    vowels: List[str] = ['a', 'e', 'i', 'o', 'u']
    num_vowels: int = 0
    for i in inputStr:
        if i in vowels:
            num_vowels += 1
    return num_vowels
