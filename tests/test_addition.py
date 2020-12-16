from tokens.token import Token
from tokens.number import Number
from tokens.operators import Addition
from tokens.token_queue import TokenQueue
import pytest


# fixtures

@pytest.fixture
def zero():
    return Number([0])

@pytest.fixture
def zero_large():
    return Number([0,0,0,0,0,0,0,0,0,0,0,0])

@pytest.fixture
def one():
    return Number([1])

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
def token_queue():
    token_queue = TokenQueue.get_instance()
    token_queue.clear()
    return token_queue


# simple addition

def test_simple_one_plus_one(token_queue, one):
    token_queue.put(one)
    token_queue.put(one)
    addition = Addition()
    result = addition.compute()
    assert len(result.digits) == 1
    assert result.digits[0] == 2


def test_simple_one_plus_ten(token_queue, one, ten):
    token_queue.put(one)
    token_queue.put(ten)
    addition = Addition()
    result = addition.compute()
    assert len(result.digits) == 2
    assert result.digits[0] == 1
    assert result.digits[1] == 1


def test_simple_ten_plus_one(token_queue, one, ten):
    token_queue.put(ten)
    token_queue.put(one)
    addition = Addition()
    result = addition.compute()
    assert len(result.digits) == 2
    assert result.digits[0] == 1
    assert result.digits[1] == 1


def test_simple_eight_plus_eight(token_queue, eight):
    token_queue.put(eight)
    token_queue.put(eight)
    addition = Addition()
    result = addition.compute()
    assert len(result.digits) == 2
    assert result.digits[0] == 6
    assert result.digits[1] == 1

def test_simple_ninety_nine_plus_one(token_queue, ninety_nine, one):
    token_queue.put(ninety_nine)
    token_queue.put(one)
    addition = Addition()
    result = addition.compute()
    assert len(result.digits) == 3
    assert result.digits[0] == 0
    assert result.digits[1] == 0
    assert result.digits[2] == 1

def test_simple_zero_plus_zero_large(token_queue, zero, zero_large):
    token_queue.put(zero)
    token_queue.put(zero_large)
    addition = Addition()
    result = addition.compute()
    assert len(result.digits) == 1
    assert result.digits[0] == 0
