from . import Token, Number


class TokenStack:
    stack: list
    Instance = None

    def __init__(self):
        self.stack = []

    @staticmethod
    def get_instance():
        if TokenStack.Instance is None:
            TokenStack.Instance = TokenStack()
        return TokenStack.Instance

    def empty(self):
        return len(self.stack) == 0

    def clear(self):
        while not len(self.stack) == 0:
            self.stack.pop()

    def push(self, token: Token):
        self.stack.append(token)

    def pop(self) -> Number:
        if self.empty():
            return None
        token = self.stack.pop()
        return token.compute()
