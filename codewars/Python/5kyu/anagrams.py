# anagrams.py

__author__ = awakenedhaki

from typing import List

def anagrams(word: str, words: List[str]) -> List[str]:
    '''
    Returns all anagrams of a word in a list of words.

    :param word: str
    :param words: List of str
    :return: Returns a list of words that are anagrams
    '''
    word: str = sorted(word)
    anagrams: List[str] = []
    for s in words:
        letters: str = sorted(s)
        if word == letters:
            anagrams.append(s)
    return anagrams
