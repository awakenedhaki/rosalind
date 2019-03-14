# zeros_to_end.py

# author: awakenedhaki

def move_zeros(array):
    new_array = []
    zeros: int = []
    while array:
        popped = array.pop()
        if popped == 0 and popped is not False:
            zeros.append(0)
        else:
            new_array.insert(0, popped)
    return new_array + zeros
