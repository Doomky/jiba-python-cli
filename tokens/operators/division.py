from tokens.number import Number, Sign
from tokens.operator import Operator
from tokens.operators.addition import Addition
from tokens.operators.subtraction import Subtraction
from tokens.token_queue import TokenQueue




class Division(Operator):

    def compute(self) -> Number:
        a: Number = TokenQueue.get_instance().get_next()
        b: Number = TokenQueue.get_instance().get_next()
        return self.compute_with_numbers(a, b)

    def compute_with_numbers(self, a: Number, b: Number) -> Number:
        sign = Sign.positive if a.sign == b.sign else Sign.negative
        a.sign = Sign.positive
        b.sign = Sign.positive
        one = Number([1])
        res = Number([0])
        while a > b or a == b:
            res = Addition().compute_with_numbers(res, one)
            a = Subtraction().compute_with_numbers(a, b)
        res.sign = sign
        return res
