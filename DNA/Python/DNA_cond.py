import os
import sys

home = os.getenv('HOME')
sys.path.append(home + '/github/rosalind_scraper')
import tester
# Run in command-line with $python DNA_cond.py file-path

def count_nt(dna: str) -> tuple:
    '''
    Count nucleotides using for loop and if statements.
    '''
    a, c, g, t = 0, 0, 0, 0 # Type: tuple(int)
    for nt in dna:
        if nt == "A":
            a += 1
        elif nt == "C":
            c += 1
        elif nt == "G":
            g += 1
        elif nt == "T":
            t += 1
    return a, c, g, t

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
    except (FileNotFoundError, IndexError):
        print("Run program using $python DNA_cond.py file-path")
    finally:
        with open(filename, 'r') as infile:
            sequence = infile.readline()
        counts = count_nt(sequence)
        print(f'{counts[0]} {counts[1]} {counts[2]} {counts[3]}')
