import sys

# Run in command-line with $python HAMM.py file-path

def point_mutations(seq1: str, seq2: str) -> int:
    '''
    Count point mutations between two given sequences of equal length.
    '''
    count = 0 # Type: int
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
    return count

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        with open(filename, 'r') as infile:
            seq1 = infile.readline()
            seq2 = infile.readline()
    except (FileNotFoundError, IndexError):
        print("Run in command-line as $python HAMM.py file-path")
    finally:
        count = point_mutations(seq1, seq2)
        print("\nSolution:")
        print(count)
