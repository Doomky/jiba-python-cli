from tokens.token import Token
from tokens.number import Number, Sign
from tokens.operators import Addition
from tokens.token_stack import TokenStack
import pytest


# fixtures

@pytest.fixture
def zero():
    return Number([0])

@pytest.fixture
def zero_large():
    return Number([0,0,0,0,0,0,0,0,0,0,0,0])

@pytest.fixture
def minus_one():
    return Number([1], Sign.negative)

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
def minus_ninety_nine():
    return Number([9, 9], Sign.negative)

@pytest.fixture
def nine_nine():
    return Number([9, 9, 9, 9, 9, 9, 9, 9, 9])

@pytest.fixture
def token_stack():
    token_stack = TokenStack.get_instance()
    token_stack.clear()
    return token_stack

# simple addition

def test_simple_one_plus_one(token_stack, one):
    token_stack.push(one)
    token_stack.push(one)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 2

def test_simple_minus_one_plus_minus_one(token_stack, minus_one):
    token_stack.push(minus_one)
    token_stack.push(minus_one)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 1
    assert result.digits[0] == 2

def test_simple_one_plus_ten(token_stack, one, ten):
    token_stack.push(one)
    token_stack.push(ten)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 1
    assert result.digits[1] == 1


def test_simple_ten_plus_one(token_stack, one, ten):
    token_stack.push(ten)
    token_stack.push(one)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 1
    assert result.digits[1] == 1


def test_simple_eight_plus_eight(token_stack, eight):
    token_stack.push(eight)
    token_stack.push(eight)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 6
    assert result.digits[1] == 1

def test_simple_ninety_nine_plus_one(token_stack, ninety_nine, one):
    token_stack.push(ninety_nine)
    token_stack.push(one)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 3
    assert result.digits[0] == 0
    assert result.digits[1] == 0
    assert result.digits[2] == 1


def test_simple_ninety_nine_plus_one(token_stack, minus_ninety_nine, minus_one):
    token_stack.push(minus_ninety_nine)
    token_stack.push(minus_one)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 3
    assert result.digits[0] == 0
    assert result.digits[1] == 0
    assert result.digits[2] == 1

def test_simple_zero_plus_zero_large(token_stack, zero, zero_large):
    token_stack.push(zero)
    token_stack.push(zero_large)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 0

def test_simple_nine_nine_plus_one(token_stack, nine_nine, one):
    token_stack.push(nine_nine)
    token_stack.push(one)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 10
    assert result.digits[0] == 0
    assert result.digits[1] == 0
    assert result.digits[2] == 0
    assert result.digits[3] == 0
    assert result.digits[4] == 0
    assert result.digits[5] == 0
    assert result.digits[6] == 0
    assert result.digits[7] == 0
    assert result.digits[8] == 0
    assert result.digits[9] == 1


# different sign

def test_simple_one_plus_minus_one(token_stack, one, minus_one):
    token_stack.push(one)
    token_stack.push(minus_one)
    addition = Addition()
    result = addition.compute()
    assert len(result.digits) == 1
    assert result.digits[0] == 0

def test_simple_one_plus_minus_ninety_nine(token_stack, one, minus_ninety_nine):
    token_stack.push(one)
    token_stack.push(minus_ninety_nine)
    addition = Addition()
    result = addition.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 2
    assert result.digits[0] == 8
    assert result.digits[1] == 9

def test_simple_minus_one_plus_one(token_stack, minus_one, one):
    token_stack.push(minus_one)
    token_stack.push(one)
    addition = Addition()
    result = addition.compute()
    assert len(result.digits) == 1
    assert result.digits[0] == 0