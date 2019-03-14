# count_smileys.py

# author: awakenedhaki

from typing import List

def count_smileys(arr: List[str]) -> int:
    '''
    Count smileys.
        - Eyes: ":" or ";"
        - Nose: "-" or "~"
        - Mouth: ")" or "D"
    '''
    import re
    pattern = re.compile('[:;][-~]?[)D]')
    count = 0
    for i in arr:
        if re.match(pattern, i):
            count += 1
    return count
