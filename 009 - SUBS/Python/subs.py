# subs.py

# author: awakenedhaki

import sys

from typing import List

def motifIndexer(seq: str, motif: str):
    indices: List[int] = []
    try:
        for i, _ in enumerate(seq):
            index = seq.index(motif, i) + 1
            indices.append(index)
    except ValueError:
        return sorted(list(set(indices)))

if __name__ == '__main__':
    try:
        filename: str = sys.argv[1]
    except FileNotFoundError:
        pass
    finally:
        with open(filename, 'r') as infile:
            seq: str = infile.readline().strip()
            motif: str = infile.readline().strip()
        indices = ' '.join(map(str, motifIndexer(seq, motif)))
        print(indices)
