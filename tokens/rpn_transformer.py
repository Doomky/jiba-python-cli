from . import Token

class TokenQueue:
    pass

class RpnTransformer:

    def __init__(self, token_list: [Token]):
        self.token_list = token_list

    def transform(self) -> TokenQueue:
        raise Exception("Could not transform token list to RPN notation")