from tokens.token import Token
from enum import Enum


class BracketType(str, Enum):
    left = "left"
    right = "right"


class Bracket(Token):

    def __init__(self, type: BracketType):
        self.type = type

    def get_type(self) -> BracketType:
        return self.type
