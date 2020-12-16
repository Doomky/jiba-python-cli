from tokens.token_parser import TokenParser
from tokens.token import Token
from tokens.number import Number
from tokens.operator import Operator

def test_single_addition():
    addition = "1 + 1"
    result: [Token] = TokenParser(addition).parse()
    assert isinstance(result[0], Number) and isinstance(result[1], Operator) and (result[2], Number)

def test_single_subtraction():
    subtraction = "1 - 1"
    result: [Token] = TokenParser(subtraction).parse()
    assert isinstance(result[0], Number) and isinstance(result[1], Operator) and (result[2], Number)

def test_single_multiplication():
    multiplication = "1 * 1"
    result: [Token] = TokenParser(multiplication).parse()
    assert isinstance(result[0], Number) and isinstance(result[1], Operator) and (result[2], Number)

def test_single_division():
    division = "1 / 1"
    result: [Token] = TokenParser(division).parse()
    assert isinstance(result[0], Number) and isinstance(result[1], Operator) and (result[2], Number)