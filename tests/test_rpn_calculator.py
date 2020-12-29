import pytest
from tokens import Token
from tokens.operators.addition import Addition
from tokens.operators.subtraction import Subtraction
from tokens.token_queue import TokenQueue
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
    token_queue: TokenQueue = TokenQueue.get_instance()
    token_queue.put(addition)
    token_queue.put(one)
    token_queue.put(one)
    number: Number = RpnCalculator(token_queue).compute()

    assert token_queue.empty()

    assert number.sign == Sign.positive
    assert len(number.digits) == 1
    assert number.digits[0] == 2


def test_compute_simple_substraction(one, subtraction):
    token_queue: TokenQueue = TokenQueue.get_instance()
    token_queue.put(subtraction)
    token_queue.put(one)
    token_queue.put(one)
    number: Number = RpnCalculator(token_queue).compute()

    assert token_queue.empty()

    assert len(number.digits) == 1
    assert number.digits[0] == 0