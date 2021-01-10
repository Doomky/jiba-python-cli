from tokens.number import Number, Sign
from tokens.operators import Power
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
def large_number():
    return Number([2, 6, 3, 8, 7, 6])


@pytest.fixture
def token_queue():
    token_queue = TokenQueue.get_instance()
    token_queue.clear()
    return token_queue


# Single digit power

def test_one_power_one(token_queue, one):
    token_queue.put(one)
    token_queue.put(one)
    power = Power()
    result = power.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_one_power_two(token_queue, one, two):
    token_queue.put(one)
    token_queue.put(two)
    power = Power()
    result = power.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_two_power_four(token_queue, two, four):
    token_queue.put(two)
    token_queue.put(four)
    power = Power()
    result = power.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 6
    assert result.digits[1] == 1


def test_eight_power_four(token_queue, eight, four):
    token_queue.put(eight)
    token_queue.put(four)
    power = Power()
    result = power.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 4
    assert result.digits[0] == 6
    assert result.digits[1] == 9
    assert result.digits[2] == 0
    assert result.digits[3] == 4
