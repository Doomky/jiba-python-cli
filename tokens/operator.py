from . import Token, Number


class Operator(Token):

    precedence: int = None
    associativity: bool = False  # False = Left, True = Right

    def __str__(self):
        raise Exception("Unknown token")

    def compute(self) -> Number:
        raise Exception("Unknown token")

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        raise Exception("Unknown token")
