import pytest
from tokens import Token
from tokens.operators.addition import Addition
from tokens.operators.subtraction import Subtraction
from tokens.token_stack import TokenStack
from tokens.rpn_calculator import RpnCalculator
from tokens.number import Number, Sign

@pytest.fixture
def addition():
    return Addition()

@pytest.fixture
def subtraction():
    return Subtraction()

@pytest.fixture
def one():
    return Number([1])

def test_compute_simple_addition(one, addition):
    token_stack: TokenStack = TokenStack.get_instance()
    token_stack.push(one)
    token_stack.push(one)
    token_stack.push(addition)
    number: Number = RpnCalculator(token_stack).compute()

    assert token_stack.empty()

    assert number.sign == Sign.positive
    assert len(number.digits) == 1
    assert number.digits[0] == 2


def test_compute_simple_substraction(one, subtraction):
    token_stack: TokenStack = TokenStack.get_instance()
    token_stack.push(one)
    token_stack.push(one)
    token_stack.push(subtraction)
    number: Number = RpnCalculator(token_stack).compute()

    assert token_stack.empty()

    assert len(number.digits) == 1
    assert number.digits[0] == 0