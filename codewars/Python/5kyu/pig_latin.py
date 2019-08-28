# pig_latin.py

__author__ = awakenedhaki

def pig_it(text: str) -> str:
    '''
    Move first character to the end and adds ay.

    :param text: str
    :return: str
    '''
    s = ''
    for i in text.split():
        if i.isalpha():
            s += f'{i[1:]}{i[0]}ay '
        else:
            s += i
    return s.rstrip()
