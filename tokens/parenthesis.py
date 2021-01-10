from tokens import Token
from enum import Enum


class ParenthesisType(str, Enum):
    left = "left"
    right = "right"


class Parenthesis(Token):

    precedence = 3

    def __init__(self, type: ParenthesisType):
        self.type = type

    def get_type(self) -> ParenthesisType:
        return self.type
