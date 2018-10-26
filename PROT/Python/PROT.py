import sys
import json

# Run in command line with $python PROT.py rna_protein.json file-path

try:
    json_file = sys.argv[1]
    with open(json_file, 'r') as json_infile:
        rna_protein_dict = json.load(json_infile)
except (IndexError, json.JSONDecodeError):
    print("Run in command-line with $python PROT.py rna-protein.json file-path")

def translate(rna: str) -> str:
    '''
    Translates RNA sequence into amino acid sequence.
    '''
    codons = [rna[i:i+3] for i in range(0, len(rna), 3)]
    protein = ''
    for codon in codons:
        protein += rna_protein_dict[codon]
    return protein

try:
    filename = sys.argv[2]
    with open(filename, 'r') as infile:
        rna = infile.readline().rstrip()
except (FileNotFoundError, IndexError):
    print("Run in command-line with $python PROT.py rna-protein.json file-path")
finally:
    protein = translate(rna)
    print("\nSolution without Biopython:")
    print(protein)

