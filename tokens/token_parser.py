from . import Token

class TokenParser:

    def __init__(self, input_str: str):
        self.input_str = input_str

    def parse(self) -> [Token]:
        raise Exception("Could not parse input");