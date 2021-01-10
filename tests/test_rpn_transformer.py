from tokens import TokenParser, Token, TokenStack, RpnTransformer, Number
from tokens.operators import Addition, Subtraction, Multiplication, Division


def test_single_addition():
    input = "1 + 1"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 3
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Addition)


def test_single_multiplication():
    input = "8 * 2"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 3
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Multiplication)


def test_multiple_addition():
    input = "2 + 3 + 4"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 5
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Addition)
    assert isinstance(token_stack_list[3], Number)
    assert isinstance(token_stack_list[4], Addition)


def test_addition_and_subtraction():
    input = "4 - 7 + 9"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 5
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Subtraction)
    assert isinstance(token_stack_list[3], Number)
    assert isinstance(token_stack_list[4], Addition)


def test_addition_and_multiplication():
    input = "4 + 3 * 2"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 5
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Number)
    assert isinstance(token_stack_list[3], Multiplication)
    assert isinstance(token_stack_list[4], Addition)


def test_multiple_operations():
    input = "7 * 8 / 2 + 4 * 2 - 1"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 11
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Multiplication)
    assert isinstance(token_stack_list[3], Number)
    assert isinstance(token_stack_list[4], Division)
    assert isinstance(token_stack_list[5], Number)
    assert isinstance(token_stack_list[6], Number)
    assert isinstance(token_stack_list[7], Multiplication)
    assert isinstance(token_stack_list[8], Addition)
    assert isinstance(token_stack_list[9], Number)
    assert isinstance(token_stack_list[10], Subtraction)


def test_addition_and_multiplication_parenthesis():
    input = "(3 + 4) * 5"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 5
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Addition)
    assert isinstance(token_stack_list[3], Number)
    assert isinstance(token_stack_list[4], Multiplication)


def test_multiple_operations_parenthesis():
    input = "(3 + 4) * (5 - 4)"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 7
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Addition)
    assert isinstance(token_stack_list[3], Number)
    assert isinstance(token_stack_list[4], Number)
    assert isinstance(token_stack_list[5], Subtraction)
    assert isinstance(token_stack_list[6], Multiplication)


def test_multiple_operations_multiple_parenthesis():
    input = "2 * (5 - (5 / 4))"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 7
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Number)
    assert isinstance(token_stack_list[3], Number)
    assert isinstance(token_stack_list[4], Division)
    assert isinstance(token_stack_list[5], Subtraction)
    assert isinstance(token_stack_list[6], Multiplication)


def test_multiple_operations_multiple_parenthesis_complex():
    input = "((7 + 5) * 9) / ((4 + 2) * 2) * (7 - 8)"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 15
    assert isinstance(token_stack_list[0], Number)
    assert isinstance(token_stack_list[1], Number)
    assert isinstance(token_stack_list[2], Addition)
    assert isinstance(token_stack_list[3], Number)
    assert isinstance(token_stack_list[4], Multiplication)
    assert isinstance(token_stack_list[5], Number)
    assert isinstance(token_stack_list[6], Number)
    assert isinstance(token_stack_list[7], Addition)
    assert isinstance(token_stack_list[8], Number)
    assert isinstance(token_stack_list[9], Multiplication)
    assert isinstance(token_stack_list[10], Division)
    assert isinstance(token_stack_list[11], Number)
    assert isinstance(token_stack_list[12], Number)
    assert isinstance(token_stack_list[13], Subtraction)
    assert isinstance(token_stack_list[14], Multiplication)


def test_global1():
    input = "(3 + 8) * (5 / 2) - 1"
    token_list: [Token] = TokenParser(input).parse()
    token_stack: TokenStack = RpnTransformer(token_list).transform()
    token_stack_list = list(token_stack.stack)
    assert len(token_stack_list) == 9
    assert isinstance(token_stack_list[0], Number) and token_stack_list[0].digits[0] == 3
    assert isinstance(token_stack_list[1], Number) and token_stack_list[1].digits[0] == 8
    assert isinstance(token_stack_list[2], Addition)
    assert isinstance(token_stack_list[3], Number) and token_stack_list[3].digits[0] == 5
    assert isinstance(token_stack_list[4], Number) and token_stack_list[4].digits[0] == 2
    assert isinstance(token_stack_list[5], Division)
    assert isinstance(token_stack_list[6], Multiplication)
    assert isinstance(token_stack_list[7], Number) and token_stack_list[7].digits[0] == 1
    assert isinstance(token_stack_list[8], Subtraction)
