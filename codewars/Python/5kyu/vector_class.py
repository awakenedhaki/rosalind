# vector_class.py

__author__ = awakenedhaki

import operator

from math import sqrt
from functools import reduce

class Vector:

    '''
    A vector object that supports:
        - addition
        - subtraction
        - dot product
        - norms

    Dundermethods could have been implements for certain function. The problem specified to define function without them.

    If dundermethods were used, we could use higher level syntax, such as +, to add vectors rather than call the method Vector.add() method.
    '''
    
    def __init__(self, args):
        self.args = tuple(args)

    def __str__(self):
        string = '('
        for i in self.args:
            string += str(i) + ','
        return string[:-1] + ')'

    def add(self, other):
        added = []
        for i, elem in enumerate(self.args):
            added.append(elem + other.args[i])
        return Vector(added)

    def subtract(self, other):
        subbed = []
        for i, elem, in enumerate(self.args):
            subbed.append(elem - other.args[i])
        return Vector(subbed)

    def dot(self, other):
        mul = [x * y for x, y in zip(self.args, other.args)]
        return reduce(operator.add, mul)

    def norm(self):
        sqr = map((lambda x: x ** 2), self.args)
        return sqrt(reduce(operator.add, sqr))

    def equals(self, other):
        return str(self.args) == str(other.args)
