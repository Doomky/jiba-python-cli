from tokens.number import Number, Sign
from tokens.operator import Operator
from tokens.token_queue import TokenQueue

def addition():
    from tokens.operators.addition import Addition
    return Addition()


class Subtraction(Operator):

    def compute(self) -> Number:
        a: Number = TokenQueue.get_instance().get_next()
        b: Number = TokenQueue.get_instance().get_next()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        if a.sign != b.sign:
            return addition()\
                .compute_with_numbers(Number(a.digits, a.sign), b.opposite_inverse())
        elif a.sign == b.sign == Sign.negative:
            return self.compute_with_numbers(b.opposite_inverse(), a.opposite_inverse())
        elif a < b:
            return Number(self.compute_with_numbers(b, a).digits, Sign.negative)
        res = []
        carry = 0
        for i in range(max(len(a), len(b))):
            ai = a[i] if len(a) > i else 0
            bi = b[i] if len(b) > i else 0
            diff = ai - bi - carry
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
