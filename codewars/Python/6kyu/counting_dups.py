# counting_dups.py

# author: awakenedhaki

from collections import Counter

def duplicate_count(text: str) -> int:
    # i is number of duplicates in text
    i: int = 0
    for k, v in Counter(text.lower()).items():
        if v > 1:
            i += 1
    return i
