from . import Token
from enum import Enum

class Sign(int, Enum):
    positive = 1
    negative = 2

class Number(Token):

    def __init__(self, digits : [int], sign = Sign.positive):
        self.digits = digits.copy()
        self.sign = sign

    def __str__(self):
        return ('' if self.sign == Sign.positive else '-').join([str(digit_int) for digit_int in self.digits])

    def compute(self):
        return self

    def opposite_inverse(self):
        Number(self.digits.copy(), Sign.positive if sign is Sign.negative else Sign.negative)
