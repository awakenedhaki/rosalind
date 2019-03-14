# alphabet_position.py

# author: awakenedhaki

def alphabet_position(text: str) -> str:
    '''
    From a string of text, return a string with the alphabet position of each letter.
    '''
    alpha = dict([(chr(i), i - 96) for i in range(97, 123)])
    string = ''
    for letter in filter(str.isalpha, text):
        try:
            string += f'{alpha[letter.lower()]} '
        except KeyError:
            continue
    return string.rstrip()
