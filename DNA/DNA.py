import sys

# Run in command-line with $python DNA.py file-path

def count_nt_v1(dna: str) -> tuple:
    '''
    Version 1
    Count nucleoides using count method.
    '''
    counts = (a, c, g, t) = (dna.count("A"),  # tuple(int)
                             dna.count("C"),
                             dna.count("G"),
                             dna.count("T"))
    return counts

def count_nt_v2(dna: str) -> tuple:
    '''
    Version 2
    Count nucleotides using for loop and if statements.
    '''
    a, c, g, t = 0, 0, 0, 0 # tuple(int)
    for nt in dna:
        if nt == "A":
            a += 1
        elif nt == "C":
            c += 1
        elif nt == "G":
            g += 1
        elif nt == "T":
            t += 1
    return a, c, g, t

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        with open(filename, 'r') as infile:
            sequence = infile.readline()
    except (FileNotFoundError, IndexError):
        print("Run in command-line with $python DNA.py file-path")
    finally:
        # Version 1
        counts_v1 = count_nt_v1(sequence)
        print("\nSolution with count method:")
        print(f'{counts_v1[0]} {counts_v1[1]} {counts_v1[2]} {counts_v1[3]}')
        # Version 2
        counts_v2 = count_nt_v2(sequence)
        print("\nSolution using for loop and if statements:")
        print(f'{counts_v2[0]} {counts_v2[1]} {counts_v2[2]} {counts_v2[3]}')
        # Using Counter from collections
        from collections import Counter
        counts = Counter(sequence) # dict
        print("\nSolution using Counter from collections module:")
        print(f'{counts["A"]} {counts["C"]} {counts["G"]} {counts["T"]}') 
