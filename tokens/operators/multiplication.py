from tokens.number import Number, Sign
from tokens.operator import Operator
from tokens.operators.addition import Addition
from tokens.token_stack import TokenStack
from command_context import CommandContext


class Multiplication(Operator):

    precedence = 2

    def __str__(self):
        return "*"

    def compute(self) -> Number:
        b: Number = TokenStack.get_instance().pop()
        a: Number = TokenStack.get_instance().pop()
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
            res = Addition().compute_with_numbers(res, Number(digits, Sign.positive))
        if a.sign != b.sign:
            res.sign = Sign.negative
        return res
