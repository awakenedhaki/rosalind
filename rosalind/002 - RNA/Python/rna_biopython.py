import sys
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

# Run in command-line as $python RNA_biopython.py file-path

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        with open(filename, 'r') as infile:
            dna = infile.readline()
    except (FileNotFoundError, IndexError):
        print("\nRun in command-line as $python RNA_biopython.py file-path")
    finally:
        dna_seq = Seq(dna, generic_dna)
        rna_seq = dna_seq.transcribe()
        print("\nSolution with Biopython")
        print(rna_seq)
