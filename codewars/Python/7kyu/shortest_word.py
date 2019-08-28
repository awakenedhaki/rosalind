# shortest_word.py

__author__: awakenedhaki

def find_short(s: str) -> int:
    '''
    Finds shortest word length
    '''
    shortest = min(map((lambda w: len(w)), s.split(' ')))
    return shortest
