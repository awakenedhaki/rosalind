import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_protein
from Bio.SeqUtils import molecular_weight

# Run in command line $python PRMT_biopython file-path

try:
    filename = sys.argv[1]
    with open(filename, 'r') as infile:
        protein = infile.read()
except (FileNotFoundError, IndexError):
    print("\nRun in command line: $python PRMT_bipython.py file-path")
finally:
    prot_seq = Seq(protein, generic_protein)
    prot_mass = molecular_weight(prot_seq, monoisotopic = True)
    print("\nBiopython solution:")
    print(prot_mass)
