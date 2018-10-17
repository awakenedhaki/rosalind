import sys
import json

# Run in command-line with $python PRMT.py protein-mass.json file-path

# Load json file
try:
    json_filename = sys.argv[1]
    with open(json_filename, 'r') as json_infile:
        protein_mass_dict = json.load(json_infile)
except (IndexError, json.JSONDecodeError):
    print("\nRun in command-line with $python PRMT.py protein-mass.json file-path")

def protein_mass(protein: str) -> float:
    '''
    Calculate monoisotopic mass of protein sequence.
    Mass values used were those referenced in Rosalind.
    '''
    mass = 0.0 # float
    for aa in protein:
        mass += protein_mass_dict[aa]
    return mass

if __name__ == "__main__":
    try:
        filename = sys.argv[2]
        with open(filename, 'r') as infile:
            protein = infile.readline().rstrip()
    except (FileNotFoundError, IndexError):
        print("\nRun in command-line with $python PRMT.py protein-mass.json file-path")
    finally:
        protein_mass = protein_mass(protein)
        print("\nSolution without Biopython:")
        print(protein_mass)
        # Using Biopython
        from Bio.Seq import Seq
        from Bio.Alphabet import generic_protein
        from Bio.SeqUtils import molecular_weight
        p_sequence = Seq(protein, generic_protein)
        prot_mass = molecular_weight(p_sequence, monoisotopic = True)
        print("\nSolution with Biopython:")
        print(prot_mass)
        print("\nBiopython monoisotopic weight answer differs from provided Rosalind protein mass table.")
