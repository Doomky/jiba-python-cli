from . import Number
from .token_stack import TokenStack


class RpnCalculator:

    def __init__(self, token_stack: TokenStack):
        self.token_stack = token_stack

    def compute(self) -> Number:
        result = self.token_stack.pop()
        if not self.token_stack.empty():
            raise ValueError("TokenQueue was not empty after RPN compute")
        return result