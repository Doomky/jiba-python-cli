from tokens.token import Token
from tokens.number import Number, Sign
from tokens.operators import Subtraction
from tokens.token_queue import TokenQueue
import pytest

# fixtures

@pytest.fixture
def one():
    return Number([1])

@pytest.fixture
def two():
    return Number([2])

@pytest.fixture
def ten():
    return Number([0, 1])

@pytest.fixture
def hundred():
    return Number([0, 0, 1])



@pytest.fixture
def token_queue():
    token_queue = TokenQueue.get_instance()
    token_queue.clear()
    return token_queue

# simple subtraction


def test_simple_two_minus_one(token_queue, one, two):
    token_queue.put(two)
    token_queue.put(one)
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_two_digits_subtraction(token_queue, ten):
    token_queue.put(Number([0, 5]))
    token_queue.put(ten)
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 0
    assert result.digits[1] == 4


def test_simple_carry(token_queue):
    token_queue.put(Number([3, 5]))
    token_queue.put(Number([5, 3]))
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 8
    assert result.digits[1] == 1


def test_leading_zero_removal(token_queue):
    token_queue.put(Number([3, 5]))
    token_queue.put(Number([1, 5]))
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 2


def test_negative_result_subtraction(token_queue, one, two):
    token_queue.put(one)
    token_queue.put(two)
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 1
    assert result.digits[0] == 1
