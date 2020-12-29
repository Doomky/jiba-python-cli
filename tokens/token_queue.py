from queue import Queue
from . import Token, Number

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

    def empty(self):
        return self.queue.empty()

    def clear(self):
        while not self.queue.empty():
            self.queue.get()

    def put(self, token: Token):
        self.queue.put(token)

    def get_next(self) -> Number:
        token = self.queue.get()
        return token.compute()
