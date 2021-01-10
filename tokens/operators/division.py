from tokens.number import Number, Sign
from tokens.operator import Operator
from tokens.token_queue import TokenQueue
from command_context import CommandContext


class DividingByZeroError(Exception):
    def __init__(self):
        super().__init__("Illegal Operation detected : Cannot divide by zero")


class Division(Operator):

    precedence = 2
    
    def compute(self) -> Number:
        a: Number = TokenQueue.get_instance().get_next()
        b: Number = TokenQueue.get_instance().get_next()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        if not b:
            raise DividingByZeroError()
        b_copy = Number(b.digits.copy())
        q = Number([0])
        r = Number(a.digits.copy())
        while r >= b_copy:
            n = len(r) - len(b_copy)
            n_digits = [0 for _ in range(n)]
            n_digits.extend(b_copy.digits)
            n_number = Number(n_digits)
            if n_number > r:
                n -= 1
                del n_number.digits[0]
            c = CommandContext.Base - 1
            cal = n_number * Number([c])
            while cal > r:
                c -= 1
                cal = n_number * Number([c])
            c_digits = [0 for _ in range(n)]
            c_digits.append(c)
            q = q + Number(c_digits)
            r = r - cal
        if a.sign != b.sign:
            q.sign = Sign.negative
        return q
