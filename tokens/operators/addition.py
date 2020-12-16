from tokens.number import Number
from tokens.operator import Operator
from tokens.token_queue import TokenQueue

class Addition(Operator):

    def compute(self) -> Number:
        a : Number = TokenQueue.get_instance().get_next()
        b : Number = TokenQueue.get_instance().get_next()

        res = Number([0])

        res.digits[0] = a.digits[0] + b.digits[0]

        return res;