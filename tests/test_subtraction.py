from tokens.token import Token
from tokens.number import Number, Sign
from tokens.operators import Subtraction
from tokens.token_stack import TokenStack
import pytest

# fixtures

@pytest.fixture
def one():
    return Number([1])

@pytest.fixture
def two():
    return Number([2])

@pytest.fixture
def ten():
    return Number([0, 1])

@pytest.fixture
def hundred():
    return Number([0, 0, 1])



@pytest.fixture
def token_stack():
    token_stack = TokenStack.get_instance()
    token_stack.clear()
    return token_stack

# simple subtraction


def test_simple_two_minus_one(token_stack, one, two):
    token_stack.push(two)
    token_stack.push(one)
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_two_digits_subtraction(token_stack, ten):
    token_stack.push(Number([0, 5]))
    token_stack.push(ten)
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 0
    assert result.digits[1] == 4

def test_different_digits_number_subtraction(token_stack, ten, one):
    token_stack.push(one)
    token_stack.push(ten)
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 1
    assert result.digits[0] == 9

def test_simple_carry(token_stack):
    token_stack.push(Number([3, 5]))
    token_stack.push(Number([5, 3]))
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 8
    assert result.digits[1] == 1


def test_leading_zero_removal(token_stack):
    token_stack.push(Number([3, 5]))
    token_stack.push(Number([1, 5]))
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 2


def test_negative_result_subtraction(token_stack, one, two):
    token_stack.push(one)
    token_stack.push(two)
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_negative_numbers_subtraction(token_stack):
    token_stack.push(Number([4, 5], Sign.negative))
    token_stack.push(Number([2, 6], Sign.negative))
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 8


def test_opposite_signs_numbers_subtraction1(token_stack):
    token_stack.push(Number([2, 1], Sign.negative))
    token_stack.push(Number([3, 1], Sign.positive))
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 2
    assert result.digits[0] == 5
    assert result.digits[1] == 2


def test_opposite_signs_numbers_subtraction2(token_stack):
    token_stack.push(Number([2, 1], Sign.positive))
    token_stack.push(Number([3, 1], Sign.negative))
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 5
    assert result.digits[1] == 2


def test_different_size_numbers(token_stack, ten, one):
    token_stack.push(ten)
    token_stack.push(one)
    subtraction = Subtraction()
    result = subtraction.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 9
