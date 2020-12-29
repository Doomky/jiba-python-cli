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
def token_queue():
    token_queue = TokenQueue.get_instance()
    token_queue.clear()
    return token_queue

# simple subtraction

def test_simple_two_minus_one(token_queue, one, two):
    token_queue.put(one)
    token_queue.put(two)
    addition = Subtraction()
    result = addition.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1

