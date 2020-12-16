from queue import Queue
from . import Token, Number


# forward declaration for type checking
class TokenQueue:
    pass


class TokenQueue:
    Instance = None

    def __init__(self):
        self.queue = Queue()

    @staticmethod
    def get_instance() -> TokenQueue:
        if TokenQueue.Instance is None:
            TokenQueue.Instance = TokenQueue()
        return TokenQueue.Instance

    def put(self, token: Token):
        self.queue.put(token)

    def get_next(self) -> Number:
        token = self.queue.get()
        return token.compute()
