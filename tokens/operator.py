from . import Token, Number


class Operator(Token):

    def __str__(self):
        raise Exception("Unknown token")

    def compute(self) -> Number :
        raise Exception("Unknown token")
        
    def compute_with_numbers(self, a : Number, b : Number) -> Number:
        raise Exception("Unknown token")
