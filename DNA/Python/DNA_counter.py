import sys
from collections import Counter

# Run in command line with $python DNA_counter.py file-path

try:
    filename = sys.argv[1]
    with open(filename, 'r') as infile:
        sequence = infile.readline()
except (FileNotFoundError, IndexError):
    print("Run in command line with $python DNA_counter.py file-path")
finally:
    counts = Counter(sequence) # Type: Dict[str, int]
    print(f'{counts["A"]} {counts["C"]} {counts["G"]} {counts["T"]}') 
