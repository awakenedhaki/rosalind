# anagrams.py

# author: awakenedhaki

from typing import List

def anagrams(word: str, words: List[str]) -> List[str]:
    '''
    Returns all anagrams of a word in a list of words.
    '''
    word: str = sorted(word)
    anagrams: List[str] = []
    for s in words:
        letters: str = sorted(s)
        if word == letters:
            anagrams.append(s)
    return anagrams
