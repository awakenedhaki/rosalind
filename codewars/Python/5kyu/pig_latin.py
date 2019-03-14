# pig_latin.py

# author: awakenedhaki

def pig_it(text):
    '''
    Move first character to the end and adds ay.
    '''
    s = ''
    for i in text.split():
        if i.isalpha():
            s += f'{i[1:]}{i[0]}ay '
        else:
            s += i
    return s.rstrip()
