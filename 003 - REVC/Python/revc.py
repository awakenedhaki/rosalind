import sys
import json

# Run in command line as $python REVC.py complement.json file-path

try:
    json_file = sys.argv[1]
    with open(json_file, 'r') as json_file:
        complement_dict = json.load(json_file)
except (IndexError, json.JSONDecodeError):
    print("Run in command-line as $python REVC.py complement.json file-path")

def reverse_complement(dna: str) -> str:
    '''
    Return reverse complement of given dna sequence.
    '''
    complement = ''
    for nt in dna:
        complement += complement_dict[nt]
    rev_complement = complement[::-1]
    return rev_complement

try:
    filename = sys.argv[2]
    with open(filename, 'r') as infile:
        dna = infile.readline().rstrip()
except (FileNotFoundError, IndexError):
    print("Run in command-line as $python REVC.py complement.json file-path")
finally:
    rev_complement = reverse_complement(dna)
    print("\nSolution without Biopython:")
    print(rev_complement)
