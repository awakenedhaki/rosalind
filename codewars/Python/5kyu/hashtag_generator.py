# hashtag_generator.py

__author__ = awakenedhaki

def generate_hashtag(s: str) -> str:
    '''
    Create a hashtag:
        - Every word is capitalize
        - No longer than 140 characters

    :param s: str
    :return: A string prefixed with #
    '''
    hashtag = ''.join([i.capitalize() for i in s.split()])
    if hashtag == '' or len(hashtag) + 1 > 140:
        return False
    return '#%s' % hashtag
