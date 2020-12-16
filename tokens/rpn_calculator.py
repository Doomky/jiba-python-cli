from . import Number

class TokenQueue:
    pass

class RpnCalculator:

    def __init__(self, token_queue: TokenQueue):
        self.token_queue = token_queue

    def compute(self) -> Number:
        raise Exception("Could not compute tokenQueue")
