from .token import Token
from .number import Number
from .parenthesis import Parenthesis, ParenthesisType
from .operators import Addition, Subtraction, Multiplication, Division, Power


class TokenParser:
    def __init__(self, input_str: str):
        self.input_str = input_str

    @staticmethod
    def _parse_number_token(i: int, input_str: str, result_tokens: [Token]):
        digits = [int(input_str[i])]
        i += 1
        while i < len(input_str) and '0' <= input_str[i] <= '9':
            digits.append(int(input_str[i]))
            i += 1
        digits.reverse()
        result_tokens.append(Number(digits))
        return i

    @staticmethod
    def _parse_addition_token(i: int, result_tokens: [Token]):
        result_tokens.append(Addition())
        return i + 1

    @staticmethod
    def _parse_subtraction_token(i: int, result_tokens: [Token]):
        result_tokens.append(Subtraction())
        return i + 1

    @staticmethod
    def _parse_multiplication_token(i: int, result_tokens: [Token]):
        result_tokens.append(Multiplication())
        return i + 1

    @staticmethod
    def _parse_division_token(i: int, result_tokens: [Token]):
        result_tokens.append(Division())
        return i + 1

    @staticmethod
    def _parse_power_token(i: int, result_tokens: [Token]):
        result_tokens.append(Power())
        return i + 1

    @staticmethod
    def _parse_bracket_token(i: int, result_tokens: [Token], bracket_type: ParenthesisType):
        result_tokens.append(Parenthesis(bracket_type))
        return i + 1

    def parse(self) -> [Token]:
        result_tokens: [Token] = []
        input_str = self.input_str
        i = 0
        while i < len(input_str):
            char_i = input_str[i]
            if '0' <= char_i <= '9':
                i = self._parse_number_token(i, input_str, result_tokens)
            elif char_i == '+':
                i = self._parse_addition_token(i, result_tokens)
            elif char_i == '-':
                i = self._parse_subtraction_token(i, result_tokens)
            elif char_i == '*':
                i = self._parse_multiplication_token(i, result_tokens)
            elif char_i == '/':
                i = self._parse_division_token(i, result_tokens)
            elif char_i == '^':
                i = self._parse_power_token(i, result_tokens)
            elif char_i == '(':
                i = self._parse_bracket_token(i, result_tokens, ParenthesisType.left)
            elif char_i == ')':
                i = self._parse_bracket_token(i, result_tokens, ParenthesisType.right)
            elif char_i == ' ':
                i += 1
            else:
                raise Exception("Could not parse character: " + char_i)
        return result_tokens
