import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

# Run in command line with $python PROT_biopython.py file-path

try:
    filename = sys.argv[1]
    with open(filename, 'r') as infile:
        sequence = infile.read()
except (FileNotFoundError, IndexError):
    print("\nRun with command line with $python PROT_biopython file-path")
finally:
    rna_seq = Seq(sequence, generic_rna)
    protein_seq = rna_seq.translate()
    print("\nSolution with Biopython:")
    print(protein_seq)
