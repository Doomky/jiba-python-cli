from . import Number
from .token_queue import TokenQueue


class RpnCalculator:

    def __init__(self, token_queue: TokenQueue):
        self.token_queue = token_queue

    def compute(self) -> Number:
        result = self.token_queue.get_next()
        if not self.token_queue.empty():
            raise ValueError("TokenQueue was not empty after RPN compute")
        return result