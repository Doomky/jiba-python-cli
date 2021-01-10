from tokens.number import Number, Sign
from tokens.operators import Division, DividingByZeroError
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
def three():
    return Number([3])


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


# Single digit division

def test_one_divided_by_one(token_stack, one):
    token_stack.push(one)
    token_stack.push(one)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_one_divided_by_two(token_stack, one, two):
    token_stack.push(one)
    token_stack.push(two)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 0


def test_four_divided_by_two(token_stack, four, two):
    token_stack.push(four)
    token_stack.push(two)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 2


def test_eight_divided_by_three(token_stack, eight, three):
    token_stack.push(eight)
    token_stack.push(three)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 2


def test_zero_divided_by_two(token_stack, zero, two):
    token_stack.push(zero)
    token_stack.push(two)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 0


# Multiple digits division

def test_ninety_nine_divided_by_one(token_stack, ninety_nine, one):
    token_stack.push(ninety_nine)
    token_stack.push(one)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 2
    assert result.digits[0] == 9
    assert result.digits[1] == 9


def test_large_number_divided_by_ninety_nine(token_stack, large_number, ninety_nine):
    token_stack.push(large_number)
    token_stack.push(ninety_nine)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 4
    assert result.digits[0] == 2
    assert result.digits[1] == 5
    assert result.digits[2] == 8
    assert result.digits[3] == 6


# Negative numbers division

def test_one_divided_by_minus_one(token_stack, one, minus_one):
    token_stack.push(one)
    token_stack.push(minus_one)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_minus_one_divided_by_one(token_stack, minus_one, one):
    token_stack.push(minus_one)
    token_stack.push(one)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.negative
    assert len(result.digits) == 1
    assert result.digits[0] == 1


def test_minus_one_divided_by_minus_one(token_stack, minus_one):
    token_stack.push(minus_one)
    token_stack.push(minus_one)
    division = Division()
    result = division.compute()
    assert result.sign == Sign.positive
    assert len(result.digits) == 1
    assert result.digits[0] == 1


# Dividing by zero

def test_dividing_by_zero(token_stack, one, zero):
    with pytest.raises(DividingByZeroError):
        token_stack.push(one)
        token_stack.push(zero)
        division = Division()
        division.compute()
