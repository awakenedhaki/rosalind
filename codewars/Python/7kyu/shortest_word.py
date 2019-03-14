# shortest_word.py

# author: awakenedhaki

def find_short(s: str) -> int:
    '''
    Finds shortest word length
    '''
    shortest = min(map((lambda w: len(w)), s.split(' ')))
    return shortest
