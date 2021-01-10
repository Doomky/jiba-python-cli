from tokens.number import Number, Sign
from tokens.operators import Multiplication
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


# Single digit multiplication

def test_one_times_one(token_stack, one):
    token_stack.push(one)
    token_stack.push(one)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_one_times_two(token_stack, one, two):
    token_stack.push(one)
    token_stack.push(two)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 2


def test_two_times_four(token_stack, two, four):
    token_stack.push(two)
    token_stack.push(four)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 8


def test_eight_times_four(token_stack, eight, four):
    token_stack.push(eight)
    token_stack.push(four)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 2
    assert result.digits[1] == 3


# Multiple digits multiplication

def test_ninety_nine_times_large_number(token_stack, ninety_nine, large_number):
    token_stack.push(ninety_nine)
    token_stack.push(large_number)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 8
    assert result.digits[0] == 8
    assert result.digits[1] == 3
    assert result.digits[2] == 8
    assert result.digits[3] == 7
    assert result.digits[4] == 5
    assert result.digits[5] == 1
    assert result.digits[6] == 7
    assert result.digits[7] == 6


def test_large_number_times_ninety_nine(token_stack, large_number, ninety_nine):
    token_stack.push(large_number)
    token_stack.push(ninety_nine)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 8
    assert result.digits[0] == 8
    assert result.digits[1] == 3
    assert result.digits[2] == 8
    assert result.digits[3] == 7
    assert result.digits[4] == 5
    assert result.digits[5] == 1
    assert result.digits[6] == 7
    assert result.digits[7] == 6


def test_nine_nine_times_nine_nine(token_stack, nine_nine):
    token_stack.push(nine_nine)
    token_stack.push(nine_nine)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 18
    assert result.digits[0] == 1
    assert result.digits[1] == 0
    assert result.digits[2] == 0
    assert result.digits[3] == 0
    assert result.digits[4] == 0
    assert result.digits[5] == 0
    assert result.digits[6] == 0
    assert result.digits[7] == 0
    assert result.digits[8] == 0
    assert result.digits[9] == 8
    assert result.digits[10] == 9
    assert result.digits[11] == 9
    assert result.digits[12] == 9
    assert result.digits[13] == 9
    assert result.digits[14] == 9
    assert result.digits[15] == 9
    assert result.digits[16] == 9
    assert result.digits[17] == 9


# Numbers with zeroes multiplication

def test_ten_times_ten(token_stack, ten):
    token_stack.push(ten)
    token_stack.push(ten)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 3
    assert result.digits[0] == 0
    assert result.digits[1] == 0
    assert result.digits[2] == 1


# By zero multiplication

def test_zero_times_large_number(token_stack, zero, large_number):
    token_stack.push(zero)
    token_stack.push(large_number)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 0


def test_large_number_times_zero(token_stack, large_number, zero):
    token_stack.push(large_number)
    token_stack.push(zero)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 0


# Negative numbers multiplication

def test_one_times_minus_one(token_stack, one, minus_one):
    token_stack.push(one)
    token_stack.push(minus_one)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_minus_one_times_one(token_stack, minus_one, one):
    token_stack.push(minus_one)
    token_stack.push(one)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_minus_one_times_minus_one(token_stack, minus_one):
    token_stack.push(minus_one)
    token_stack.push(minus_one)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1
