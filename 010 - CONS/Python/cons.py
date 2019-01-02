# cons.py

# author: awakenedhaki

# Run in command line: $python script-path file-path

import sys

from collections import Counter
from typing import Iterable, List

def consensus(counts: List[Counter]) -> str:
    '''
    Consensus sequence for the collection of sequences.
    '''
    string = ''
    for count in counts:
        nt, _ = count.most_common(1)[0]
        string += nt
    return string

def profile(sequences: List[str]) -> List[Counter]:
    '''
    A profile matrix for the collection of sequences.
    '''
    nts: set = {'A', 'T', 'G', 'C'}
    occur: List[Counter] = []
    for seq in sequences:
        counts = Counter(seq)
        diff: set = nts - set(counts.keys())
        for nt in diff:
            counts[nt] = 0
        occur.append(counts)
    return occur

def transpose_strings(strings: Iterable[str]):
    '''
    Transpose list of strings.
    Assume: all strings have the same length.

    Example:
        transpose_string(['ab', 'ab']) -> ['aa', 'bb']
    '''
    return zip(*map(list, strings))

def read_fasta(filename: str) -> List[str]:
    '''
    Parse FASTA into list of sequences.
    '''
    with open(filename, 'r') as infile:
        line: str = infile.readline().strip()
        sequences = []
        sequence = ''
        while line:
            if line.startswith('>') and sequence != '':
                sequences.append(sequence)
                sequence = ''
            elif not line.startswith('>'):
                sequence += line
            line = infile.readline().strip()
        sequences.append(sequence)
    return sequences

def print_profile(sequences: Iterable[str]):
    '''
    Print consensus sequence and its profile
    '''
    counts: List[Counter] = profile(sequences)
    consensus_seq: str = consensus(counts)
    x = a, c, g, t = [], [], [], []
    for count in counts:
        a.append(str(count['A']))
        c.append(str(count['C']))
        g.append(str(count['G']))
        t.append(str(count['T']))
    print(consensus_seq)
    print(f'A: {" ".join(a)}')
    print(f'C: {" ".join(c)}')
    print(f'G: {" ".join(g)}')
    print(f'T: {" ".join(t)}')

if __name__ == '__main__':
    try:
        filename: str = sys.argv[1]
        sequences: List[str] = read_fasta(filename)
    except IndexError:
        print('Run in command line: $python script-path file-path')
    else:
        transposed = transpose_strings(sequences)
        print_profile(transposed)