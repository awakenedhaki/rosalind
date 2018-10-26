import sys

# Run in command line as $python RNA.py file-path

def transcribe(dna: str) -> str:
    '''
    Transcribe DNA sequence, converting "T" to "U"
    '''
    rna = dna.replace("T", "U")
    return rna

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        with open(filename, 'r') as infile:
            dna = infile.readline()
    except (FileNotFoundError, IndexError):
        print("\nRun in command-line as $python RNA.py file-path")
    finally:
        rna = transcribe(dna)
        print("\nSolution without Biopython:")
        print(rna)
