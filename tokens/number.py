from . import Token
from enum import Enum


class Sign(int, Enum):
    positive = 1
    negative = 2

    @staticmethod
    def opposite(number):
        if number == Sign.positive:
            return Sign.negative
        else:
            return Sign.positive


class Number(Token):
    def __init__(self, digits: [int], sign=Sign.positive):
        self.digits = digits.copy()
        self.sign = sign

    def __str__(self):
        return ('' if self.sign == Sign.positive else '-').join([str(digit_int) for digit_int in self.digits])

    def __len__(self):
        return len(self.digits)

    def __getitem__(self, index: int):
        return self.digits[index]

    def __eq__(self, other):
        return self.sign == other.sign\
               and len(self) == len(other)\
               and all([self[i] == other[i] for i in range(len(self))])

    def __gt__(self, other):
        if (self.sign == other.sign == Sign.positive and len(self) > len(other))\
            or (self.sign == other.sign == Sign.negative and len(self) < len(other))\
                or (self.sign == Sign.positive != other.sign):
            return True
        elif (self.sign == other.sign == Sign.positive and len(self) < len(other)) \
                or (self.sign == other.sign == Sign.negative and len(self) > len(other)) \
                or (self.sign == Sign.negative != other.sign):
            return False
        for i in range(len(self) - 1, -1, -1):
            if self[i] < other[i]:
                return self.sign == Sign.negative
            if self[i] > other[i]:
                return self.sign == Sign.positive
        return False

    def compute(self):
        return self

    def opposite_inverse(self):
        return Number(self.digits.copy(), Sign.opposite(self.sign))
