from tokens.number import Number
from tokens.operator import Operator
from tokens.token_queue import TokenQueue


class Subtraction(Operator):
    def compute(self) -> Number:
        a: Number = TokenQueue.get_instance().get_next()
        b: Number = TokenQueue.get_instance().get_next()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        diff = a.digits[0] - b.digits[0]
        return Number([diff])
