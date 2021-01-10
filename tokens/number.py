from . import Token
from enum import Enum


def addition():
    from tokens.operators.addition import Addition
    return Addition()


def subtraction():
    from tokens.operators.subtraction import Subtraction
    return Subtraction()


def multiplication():
    from tokens.operators.multiplication import Multiplication
    return Multiplication()


def division():
    from tokens.operators.division import Division
    return Division()


class Sign(int, Enum):
    positive = 1
    negative = 2

    def __bool__(self):
        return self == Sign.positive

    def __neg__(self):
        if self:
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

    def __delitem__(self, key):
        del self.digits[key]

    def __setitem__(self, key, value):
        self.digits[key] = value

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

    def __lt__(self, other):
        return other > self

    def __le__(self, other):
        return not (self > other)

    def __ne__(self, other):
        return not (self == other)

    def __ge__(self, other):
        return not (self < other)

    def __bool__(self):
        for i in self.digits:
            if i != 0:
                return True
        return False

    def __add__(self, other):
        return addition().compute_with_numbers(self, other)

    def __sub__(self, other):
        return subtraction().compute_with_numbers(self, other)

    def __mul__(self, other):
        return multiplication().compute_with_numbers(self, other)

    def __truediv__(self, other):
        return division().compute_with_numbers(self, other)

    def __neg__(self):
        return Number(self.digits.copy(), Sign(-self.sign))

    def compute(self):
        return self
