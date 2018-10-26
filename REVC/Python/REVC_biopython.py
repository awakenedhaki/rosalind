import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

# Run in command line as $python REVC.py file-path

try:
    filename = sys.argv[1]
    with open(filename, 'r') as infile:
        dna = infile.readline().rstrip()
except (FileNotFoundError, IndexError):
    print("Run in command-line as $python REVC.py complement.json file-path")
finally:
    dna_seq = Seq(dna, generic_dna)
    rev_complement_seq = dna_seq.reverse_complement()
    print("\nSolution with Biopython:")
    print(rev_complement_seq)
