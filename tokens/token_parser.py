from . import Token
from . import Number
from . import Operator
from enum import Enum
import re


class TokenType(int, Enum):
    number = 0
    op_add = 1
    op_sub = 2
    op_mul = 3
    op_div = 4


class TokenParser:
    def __init__(self, input_str: str):
        self.input_str = input_str

    def _parse_number_token(self, i: int, input_str: str, result_tokens: [Token]):
        result_tokens.append(Number([int(input_str[i])]))

    def _parse_operator_token(self, i: int, input_str: str, result_tokens: [Token]):
        result_tokens.append(Operator())

    def parse(self) -> [Token]:
        result_tokens: [Token] = []

        input_str = self.input_str
        for i in range(len(input_str)):
            char_i = input_str[i]
            if '0' <= char_i <= '9':
                self._parse_number_token(i, input_str, result_tokens)
            elif char_i == '+':
                self._parse_operator_token(i, input_str, result_tokens)
            elif char_i == '-':
                self._parse_operator_token(i, input_str, result_tokens)
            elif char_i == '*':
                self._parse_operator_token(i, input_str, result_tokens)
            elif char_i == '/':
                self._parse_operator_token(i, input_str, result_tokens)

        return result_tokens
