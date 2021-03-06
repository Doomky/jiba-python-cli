from tokens.number import Number, Sign
from tokens.operator import Operator
from tokens.token_stack import TokenStack
from command_context import CommandContext


class Subtraction(Operator):

    precedence = 1

    def __str__(self):
        return "-"

    def compute(self) -> Number:
        b: Number = TokenStack.get_instance().pop()
        a: Number = TokenStack.get_instance().pop()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        if a.sign != b.sign:
            return Number(a.digits, a.sign) + (-b)
        elif a.sign == b.sign == Sign.negative:
            return (-b) - (-a)
        elif a < b:
            return Number((b - a).digits, Sign.negative)
        res = []
        carry = 0
        b_len = len(b)
        a_len = len(a)
        for i in range(max(a_len, b_len)):
            diff = (0 if i >= a_len else a[i]) - (0 if i >= b_len else b[i]) - carry
            if diff < 0:
                diff += CommandContext.Base
                carry = 1
            else:
                carry = 0
            res.append(diff)
        real_res_len = len(res)
        for digit in res[::-1]:
            if digit == 0:
                real_res_len -= 1
            else:
                break
        if real_res_len <= 1:
            return Number([res[0]])
        else:
            return Number(res[:real_res_len])
