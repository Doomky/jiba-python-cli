from tokens.number import Number, Sign
from tokens.operator import Operator
from tokens.token_queue import TokenQueue
from command_context import CommandContext


class Multiplication(Operator):

    precedence = 2
    
    def compute(self) -> Number:
        a: Number = TokenQueue.get_instance().get_next()
        b: Number = TokenQueue.get_instance().get_next()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        res = Number([0])
        for offset, i in enumerate(a.digits):
            digits = [0 for _ in range(offset)]
            carry_over = 0
            for index, j in enumerate(b.digits):
                compute = i * j + carry_over
                digits.append(compute % CommandContext.Base)
                carry_over = compute // CommandContext.Base
            if carry_over != 0:
                digits.append(carry_over)
            else:
                while len(digits) > 1 and digits[-1] == 0:
                    digits.pop()
            res = res + Number(digits, Sign.positive)
        if a.sign != b.sign:
            res.sign = Sign.negative
        return res
