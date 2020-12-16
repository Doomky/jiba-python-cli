from tokens.token import Token
from tokens.number import Number
from tokens.operators import Addition
from tokens.token_queue import TokenQueue
import pytest

# fixtures

@pytest.fixture
def one():
    return Number([1])

# simple addition

def test_simple_single_digit_addition(one):
    token_queue = TokenQueue.get_instance()
    token_queue.put(one)
    token_queue.put(one)
    addition = Addition()
    result = addition.compute()
    assert len(result.digits) == 1
    assert result.digits[0] == 2
