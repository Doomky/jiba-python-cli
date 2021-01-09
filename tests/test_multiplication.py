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
def large_number():
    return Number([2, 6, 3, 8, 7, 6])


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


# Mulitple digits multiplication

def test_ninety_nine_times_large_number(token_queue, ninety_nine, large_number):
    token_queue.put(ninety_nine)
    token_queue.put(large_number)
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


def test_large_number_times_ninety_nine(token_queue, large_number, ninety_nine):
    token_queue.put(large_number)
    token_queue.put(ninety_nine)
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


def test_nine_nine_times_nine_nine(token_queue, nine_nine):
    token_queue.put(nine_nine)
    token_queue.put(nine_nine)
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

def test_ten_times_ten(token_queue, ten):
    token_queue.put(ten)
    token_queue.put(ten)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 3
    assert result.digits[0] == 0
    assert result.digits[1] == 0
    assert result.digits[2] == 1


# By zero multiplication

def test_zero_times_large_number(token_queue, zero, large_number):
    token_queue.put(zero)
    token_queue.put(large_number)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 0


def test_large_number_times_zero(token_queue, large_number, zero):
    token_queue.put(large_number)
    token_queue.put(zero)
    multiplication = Multiplication()
    result = multiplication.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 0
    