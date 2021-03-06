from tokens.number import Number, Sign
from tokens.operator import Operator
from tokens.token_stack import TokenStack
from command_context import CommandContext


class Addition(Operator):

    precedence = 1

    def __str__(self):
        return "+"

    def compute(self) -> Number:
        b: Number = TokenStack.get_instance().pop()
        a: Number = TokenStack.get_instance().pop()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        if a.sign != b.sign:
            if b.sign == Sign.negative:
                return a - (-b)
            else:
                return b - (-a)

        a_digits = a.digits.copy()
        b_digits = b.digits.copy()

        while len(a_digits) < len(b_digits):
            a_digits.append(0)

        while len(b_digits) < len(a_digits):
            b_digits.append(0)

        res_digits = [x + y for x, y in zip(a_digits, b_digits)]

        carry_over = 0
        for i in range(len(res_digits)):
            res_digits[i] += carry_over
            carry_over = res_digits[i] // CommandContext.Base
            res_digits[i] = res_digits[i] % CommandContext.Base

        if carry_over != 0:
            res_digits.append(carry_over)
        else:
            while len(res_digits) > 1 and res_digits[-1] == 0:
                res_digits.pop()

        return Number(res_digits, a.sign)
