from tokens.token import Token
from tokens.number import Number
from tokens.operators import Addition
from tokens.token_queue import TokenQueue
import pytest


# fixtures

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