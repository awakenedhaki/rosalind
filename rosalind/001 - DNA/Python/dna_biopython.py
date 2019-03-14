import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

# Run in command-line with $python DNA_biopython.py file-path

try:
    filename = sys.argv[1]
    with open(filename, 'r') as infile:
        sequence = infile.read()
except (FileNotFoundError, IndexError):
    print("Run in command-line with $python DNA_biopython.py file-path")
finally:
    dna_seq = Seq(sequence, generic_dna)
    counts = (dna_seq.count("A"),
              dna_seq.count("C"),
              dna_seq.count("G"),
              dna_seq.count("T"))
    print(f'{counts[0]} {counts[1]} {counts[2]} {counts[3]}')
