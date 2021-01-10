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
def five():
    return Number([5])

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
    assert result == Number([1])


def test_one_power_two(token_queue, one, two):
    token_queue.put(one)
    token_queue.put(two)
    power = Power()
    result = power.compute()
    assert result == Number([1])


def test_two_power_four(token_queue, two, four):
    token_queue.put(two)
    token_queue.put(four)
    power = Power()
    result = power.compute()
    assert result == Number([6, 1])


def test_eight_power_four(token_queue, eight, four):
    token_queue.put(eight)
    token_queue.put(four)
    power = Power()
    result = power.compute()
    assert result == Number([6, 9, 0, 4])


# Complex power

def test_ninety_nine_power_five(token_queue, ninety_nine, five):
    token_queue.put(ninety_nine)
    token_queue.put(five)
    power = Power()
    result = power.compute()
    assert result == Number([9, 9, 4, 0, 0, 9, 9, 0, 5, 9])


# Zero power

def test_zero_power_four(token_queue, zero, four):
    token_queue.put(zero)
    token_queue.put(four)
    power = Power()
    result = power.compute()
    assert result == Number([0])


def test_four_power_zero(token_queue, zero, four):
    token_queue.put(four)
    token_queue.put(zero)
    power = Power()
    result = power.compute()
    assert result == Number([1])

