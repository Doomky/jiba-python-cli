from tokens.number import Number, Sign
from tokens.operator import Operator
from tokens.token_queue import TokenQueue


class Subtraction(Operator):
    def compute(self) -> Number:
        a: Number = TokenQueue.get_instance().get_next()
        b: Number = TokenQueue.get_instance().get_next()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        if a < b:
            return Number(self.compute_with_numbers(b, a).digits, Sign.negative)
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
