# dna_to_rna.py

__author__ = "awakenedhaki"

def dna_to_rna(dna: str) -> str:
    '''
    Replaces T with U.
    ASSUME: dna string is provided in proper format,
        all uppercase letter

    :param dna: str
    :return: str
    '''
    return dna.replace('T', 'U')
