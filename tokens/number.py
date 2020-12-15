from tokens import Token


class Number(Token):

    def __init__(self, digits : str):
        self.digits = [ int(digit_str) for digit_str in digits.split()]

    def __init__(self, digits : [int]):
        self.digits = digits.copy()

    def __str__(self):
        return ''.join([ str(digit_int) for digit_int in self.digits])

    def compute(self) :
        return self