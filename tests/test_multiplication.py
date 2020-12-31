from tokens.number import Number, Sign
from tokens.operators import Multiplication
from tokens.token_queue import TokenQueue
import pytest


# fixtures

@pytest.fixture
def zero():
    return Number([0])


@pytest.fixture
def zero_large():
    return Number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


@pytest.fixture
def minus_one():
    return Number([1], Sign.negative)


@pytest.fixture
def one():
    return Number([1])


@pytest.fixture
def two():
    return Number([2])


@pytest.fixture
def four():
    return Number([4])


@pytest.fixture
def eight():
    return Number([8])


@pytest.fixture
def ten():
    return Number([0, 1])


@pytest.fixture
def ninety_nine():
    return Number([9, 9])


@pytest.fixture
def minus_ninety_nine():
    return Number([9, 9], Sign.negative)


@pytest.fixture
def nine_nine():
    return Number([9, 9, 9, 9, 9, 9, 9, 9, 9])


@pytest.fixture
def token_queue():
    token_queue = TokenQueue.get_instance()
    token_queue.clear()
    return token_queue


# Single digit multiplication

def test_one_times_one(token_queue, one):
    token_queue.put(one)
    token_queue.put(one)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_one_times_two(token_queue, one, two):
    token_queue.put(one)
    token_queue.put(two)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 2


def test_two_times_four(token_queue, two, four):
    token_queue.put(two)
    token_queue.put(four)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 8


def test_eight_times_four(token_queue, eight, four):
    token_queue.put(eight)
    token_queue.put(four)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 2
    assert result.digits[1] == 3
