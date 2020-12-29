from tokens.number import Number
from tokens.operator import Operator
from tokens.token_queue import TokenQueue


class Subtraction(Operator):
    def compute(self) -> Number:
        a: Number = TokenQueue.get_instance().get_next()
        b: Number = TokenQueue.get_instance().get_next()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        res = []
        carry = 0
        for i in range(max(len(a.digits), len(b.digits))):
            diff = a.digits[i] - b.digits[i] - carry
            if diff < 0:
                diff += 10
                carry = 1
            else:
                carry = 0
            res.append(diff)
        return Number(res)
