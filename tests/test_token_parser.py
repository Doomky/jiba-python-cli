from tokens.token_parser import TokenParser
from tokens.token import Token
from tokens.number import Number
from tokens.bracket import Bracket
from tokens.operators import Addition, Subtraction, Multiplication, Division

# single digits operations


def test_single_addition():
    addition = "1 + 1"
    result: [Token] = TokenParser(addition).parse()
    assert len(result) == 3
    assert isinstance(result[0], Number)
    assert isinstance(result[1], Addition)
    assert isinstance(result[2], Number)


def test_single_subtraction():
    subtraction = "1 - 1"
    result: [Token] = TokenParser(subtraction).parse()
    assert len(result) == 3
    assert isinstance(result[0], Number)
    assert isinstance(result[1], Subtraction)
    assert isinstance(result[2], Number)


def test_single_multiplication():
    multiplication = "1 * 1"
    result: [Token] = TokenParser(multiplication).parse()
    assert len(result) == 3
    assert isinstance(result[0], Number)
    assert isinstance(result[1], Multiplication)
    assert isinstance(result[2], Number)


def test_single_division():
    division = "1 / 1"
    result: [Token] = TokenParser(division).parse()
    assert len(result) == 3
    assert isinstance(result[0], Number)
    assert isinstance(result[1], Division)
    assert isinstance(result[2], Number)


# two digits operations

def test_two_digit_number_addition():
    addition = "12 + 12"
    result: [Token] = TokenParser(addition).parse()
    assert len(result) == 3
    assert isinstance(result[0], Number)
    assert isinstance(result[1], Addition)
    assert isinstance(result[2], Number)


def test_two_digit_number_subtraction():
    subtraction = "12 - 12"
    result: [Token] = TokenParser(subtraction).parse()
    assert len(result) == 3
    assert isinstance(result[0], Number)
    assert isinstance(result[1], Subtraction)
    assert isinstance(result[2], Number)


def test_two_digit_number_multiplication():
    multiplication = "12 * 12"
    result: [Token] = TokenParser(multiplication).parse()
    assert len(result) == 3
    assert isinstance(result[0], Number)
    assert isinstance(result[1], Multiplication)
    assert isinstance(result[2], Number)


def test_two_digit_number_division():
    division = "12 / 12"
    result: [Token] = TokenParser(division).parse()
    assert len(result) == 3
    assert isinstance(result[0], Number)
    assert isinstance(result[1], Division)
    assert isinstance(result[2], Number)


def test_long_operation():
    division = "(12 + 1) * 3 / (4 + 1) "
    result: [Token] = TokenParser(division).parse()
    assert len(result) == 13
    assert isinstance(result[0], Bracket)
    assert isinstance(result[1], Number)
    assert isinstance(result[2], Addition)
    assert isinstance(result[3], Number)
    assert isinstance(result[4], Bracket)
    assert isinstance(result[5], Multiplication)
    assert isinstance(result[6], Number)
    assert isinstance(result[7], Division)
    assert isinstance(result[8], Bracket)
    assert isinstance(result[9], Number)
    assert isinstance(result[10], Addition)
    assert isinstance(result[11], Number)
    assert isinstance(result[12], Bracket)
