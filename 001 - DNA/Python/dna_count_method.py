import sys

# Run in command-line with $python DNA_count_method.py file-path

def count_nt(dna: str) -> tuple:
    '''
    Count nucleoides using count method.
    '''
    counts = (a, c, g, t) = (dna.count("A"),  # tuple(int)
                             dna.count("C"),
                             dna.count("G"),
                             dna.count("T"))
    return counts

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        with open(filename, 'r') as infile:
            sequence = infile.readline()
    except (FileNotFoundError, IndexError):
        print("Run in command line with $python DNA_count_method.py file-path")
    finally:
        counts = count_nt(sequence)
        print(f'{counts[0]} {counts[1]} {counts[2]} {counts[3]}')
