from . import Token
from . import Number
from . import Operator
import re

class TokenParser:
    def __init__(self, input_str: str):
        self.input_str = input_str

    def _parse_number_token(self, i: int, input_str: str, result_tokens: [Token]):

        digits = [int(input_str[i])]
        i+= 1

        while (i < len(input_str) and '0' <= input_str[i] <= '9'):
            digits.append(int(input_str[i]))
            i+=1
        result_tokens.append(Number(digits))
        return i

    def _parse_operator_token(self, i: int, input_str: str, result_tokens: [Token]):
        result_tokens.append(Operator())
        i+=1
        return i

    def parse(self) -> [Token]:
        result_tokens: [Token] = []

        input_str = self.input_str
        i = 0
        while i < len(input_str):
            char_i = input_str[i]
            if '0' <= char_i <= '9':
                i = self._parse_number_token(i, input_str, result_tokens)
            elif char_i == '+':
                i = self._parse_operator_token(i, input_str, result_tokens)
            elif char_i == '-':
                i = self._parse_operator_token(i, input_str, result_tokens)
            elif char_i == '*':
                i = self._parse_operator_token(i, input_str, result_tokens)
            elif char_i == '/':
                i = self._parse_operator_token(i, input_str, result_tokens)
            elif char_i == ' ':
                i += 1

        return result_tokens
