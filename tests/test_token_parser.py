from tokens.token_parser import TokenParser
from tokens.token import Token
from tokens.number import Number
from tokens.operator import Operator

# single digits operations

def test_single_addition():
    addition = "1 + 1"
    result: [Token] = TokenParser(addition).parse()
    assert len(result) == 3 and \
           isinstance(result[0], Number) and \
           isinstance(result[1], Operator) and \
           isinstance(result[2], Number)


def test_single_subtraction():
    subtraction = "1 - 1"
    result: [Token] = TokenParser(subtraction).parse()
    assert len(result) == 3 and \
           isinstance(result[0], Number) and\
           isinstance(result[1], Operator) and\
           isinstance(result[2], Number)


def test_single_multiplication():
    multiplication = "1 * 1"
    result: [Token] = TokenParser(multiplication).parse()
    assert len(result) == 3 and \
           isinstance(result[0], Number) and \
           isinstance(result[1], Operator) and \
           isinstance(result[2], Number)


def test_single_division():
    division = "1 / 1"
    result: [Token] = TokenParser(division).parse()
    assert len(result) == 3 and \
           isinstance(result[0], Number) and \
           isinstance(result[1], Operator) and \
           isinstance(result[2], Number)


# two digits operations

def test_two_digit_number_addition():
    addition = "12 + 12"
    result: [Token] = TokenParser(addition).parse()
    assert len(result) == 3 and \
           isinstance(result[0], Number) and \
           isinstance(result[1], Operator) and \
           isinstance(result[2], Number)

def test_two_digit_number_subtraction():
    subtraction = "12 - 12"
    result: [Token] = TokenParser(subtraction).parse()
    assert len(result) == 3 and \
           isinstance(result[0], Number) and \
           isinstance(result[1], Operator) and \
           isinstance(result[2], Number)

def test_two_digit_number_multiplication():
    multiplication = "12 * 12"
    result: [Token] = TokenParser(multiplication).parse()
    assert len(result) == 3 and \
           isinstance(result[0], Number) and \
           isinstance(result[1], Operator) and \
           isinstance(result[2], Number)

def test_two_digit_number_division():
    division = "12 / 12"
    result: [Token] = TokenParser(division).parse()
    assert len(result) == 3 and \
           isinstance(result[0], Number) and \
           isinstance(result[1], Operator) and \
           isinstance(result[2], Number)

def test_long_operation():
    division = "(12 + 1) * 3 / (4 + 1) "
    result: [Token] = TokenParser(division).parse()
    assert len(result) == 13 and \
           isinstance(result[0], Operator) and \
           isinstance(result[1], Number) and \
           isinstance(result[2], Operator) and \
           isinstance(result[3], Number) and \
           isinstance(result[4], Operator) and \
           isinstance(result[5], Operator) and \
           isinstance(result[6], Number) and \
           isinstance(result[7], Operator) and \
           isinstance(result[8], Operator) and \
           isinstance(result[9], Number) and \
           isinstance(result[10], Operator) and \
           isinstance(result[11], Number) and \
           isinstance(result[12], Operator)