from tokens.number import Number, Sign
from tokens.operators import Power, NegativePowerError
from tokens.token_stack import TokenStack
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
def token_stack():
    token_stack = TokenStack.get_instance()
    token_stack.clear()
    return token_stack


# Single digit power

def test_one_power_one(token_stack, one):
    token_stack.push(one)
    token_stack.push(one)
    power = Power()
    result = power.compute()
    assert result == Number([1])


def test_one_power_two(token_stack, one, two):
    token_stack.push(one)
    token_stack.push(two)
    power = Power()
    result = power.compute()
    assert result == Number([1])


def test_two_power_four(token_stack, two, four):
    token_stack.push(two)
    token_stack.push(four)
    power = Power()
    result = power.compute()
    assert result == Number([6, 1])


def test_eight_power_four(token_stack, eight, four):
    token_stack.push(eight)
    token_stack.push(four)
    power = Power()
    result = power.compute()
    assert result == Number([6, 9, 0, 4])


# Complex power

def test_ninety_nine_power_five(token_stack, ninety_nine, five):
    token_stack.push(ninety_nine)
    token_stack.push(five)
    power = Power()
    result = power.compute()
    assert result == Number([9, 9, 4, 0, 0, 9, 9, 0, 5, 9])


# Zero power

def test_zero_power_four(token_stack, zero, four):
    token_stack.push(zero)
    token_stack.push(four)
    power = Power()
    result = power.compute()
    assert result == Number([0])


def test_four_power_zero(token_stack, zero, four):
    token_stack.push(four)
    token_stack.push(zero)
    power = Power()
    result = power.compute()
    assert result == Number([1])


# Negative numbers power

def test_minus_one_power_four(token_stack, minus_one, four):
    token_stack.push(minus_one)
    token_stack.push(four)
    power = Power()
    result = power.compute()
    assert result == Number([1])


def test_minus_one_power_five(token_stack, minus_one, five):
    token_stack.push(minus_one)
    token_stack.push(five)
    power = Power()
    result = power.compute()
    assert result == Number([1], Sign.negative)


def test_one_power_minus_one(token_stack, one, minus_one):
    with pytest.raises(NegativePowerError):
        token_stack.push(one)
        token_stack.push(minus_one)
        power = Power()
        power.compute()
