from tokens.number import Number
from tokens.operator import Operator
from tokens.operators.subtraction import Subtraction
from tokens.token_queue import TokenQueue
from command_context import CommandContext

class Addition(Operator):

    def compute(self) -> Number:
        a: Number = TokenQueue.get_instance().get_next()
        b: Number = TokenQueue.get_instance().get_next()

        if a.sign != b.sign:
            return Subtraction().compute()

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
            carry_over =  res_digits[i] // CommandContext.Base
            res_digits[i] = res_digits[i] % CommandContext.Base

        if carry_over != 0:
            res_digits.append(carry_over)
        else:
            while len(res_digits) > 1 and res_digits[-1] == 0:
                    res_digits.pop()

        return Number(res_digits, a.sign)