from tokens.number import Number, Sign
from tokens.operator import Operator
from tokens.token_queue import TokenQueue


class NegativePowerError(Exception):
    def __init__(self):
        super().__init__("Illegal Operation detected : Negative power not supported")


class Power(Operator):
    precedence = 2

    def compute(self) -> Number:
        a: Number = TokenQueue.get_instance().get_next()
        b: Number = TokenQueue.get_instance().get_next()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        if not b:
            return Number([1])
        if not b.sign:
            raise NegativePowerError()
        if b == Number([1]):
            return Number(a.digits, a.sign)
        elif not b[0] % 2:
            return self.compute_with_numbers(a * a, b / Number([2]))
        else:
            return a * self.compute_with_numbers(a * a, (b - Number([1])) / Number([2]))
