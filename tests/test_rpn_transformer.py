from tokens import TokenParser, Token, TokenQueue, RpnTransformer, Number
from tokens.operators import Addition, Subtraction, Multiplication, Division


def test_single_addition():
    input = "1 + 1"
    token_list: [Token] = TokenParser(input).parse()
    token_queue: TokenQueue = RpnTransformer(token_list).transform()
    token_queue_list = list(token_queue.queue.queue)
    assert len(token_queue_list) == 3
    assert isinstance(token_queue_list[0], Number)
    assert isinstance(token_queue_list[1], Number)
    assert isinstance(token_queue_list[2], Addition)


def test_single_multiplication():
    input = "8 * 2"
    token_list: [Token] = TokenParser(input).parse()
    token_queue: TokenQueue = RpnTransformer(token_list).transform()
    token_queue_list = list(token_queue.queue.queue)
    assert len(token_queue_list) == 3
    assert isinstance(token_queue_list[0], Number)
    assert isinstance(token_queue_list[1], Number)
    assert isinstance(token_queue_list[2], Multiplication)


def test_multiple_addition():
    input = "2 + 3 + 4"
    token_list: [Token] = TokenParser(input).parse()
    token_queue: TokenQueue = RpnTransformer(token_list).transform()
    token_queue_list = list(token_queue.queue.queue)
    assert len(token_queue_list) == 5
    assert isinstance(token_queue_list[0], Number)
    assert isinstance(token_queue_list[1], Number)
    assert isinstance(token_queue_list[2], Addition)
    assert isinstance(token_queue_list[3], Number)
    assert isinstance(token_queue_list[4], Addition)


def test_addition_and_subtraction():
    input = "4 - 7 + 9"
    token_list: [Token] = TokenParser(input).parse()
    token_queue: TokenQueue = RpnTransformer(token_list).transform()
    token_queue_list = list(token_queue.queue.queue)
    assert len(token_queue_list) == 5
    assert isinstance(token_queue_list[0], Number)
    assert isinstance(token_queue_list[1], Number)
    assert isinstance(token_queue_list[2], Subtraction)
    assert isinstance(token_queue_list[3], Number)
    assert isinstance(token_queue_list[4], Addition)


def test_addition_and_multiplication():
    input = "4 + 3 * 2"
    token_list: [Token] = TokenParser(input).parse()
    token_queue: TokenQueue = RpnTransformer(token_list).transform()
    token_queue_list = list(token_queue.queue.queue)
    assert len(token_queue_list) == 5
    assert isinstance(token_queue_list[0], Number)
    assert isinstance(token_queue_list[1], Number)
    assert isinstance(token_queue_list[2], Number)
    assert isinstance(token_queue_list[3], Multiplication)
    assert isinstance(token_queue_list[4], Addition)


def test_multiple_operations():
    input = "7 * 8 / 2 + 4 * 2 - 1"
    token_list: [Token] = TokenParser(input).parse()
    token_queue: TokenQueue = RpnTransformer(token_list).transform()
    token_queue_list = list(token_queue.queue.queue)
    assert len(token_queue_list) == 11
    assert isinstance(token_queue_list[0], Number)
    assert isinstance(token_queue_list[1], Number)
    assert isinstance(token_queue_list[2], Multiplication)
    assert isinstance(token_queue_list[3], Number)
    assert isinstance(token_queue_list[4], Division)
    assert isinstance(token_queue_list[5], Number)
    assert isinstance(token_queue_list[6], Number)
    assert isinstance(token_queue_list[7], Multiplication)
    assert isinstance(token_queue_list[8], Addition)
    assert isinstance(token_queue_list[9], Number)
    assert isinstance(token_queue_list[10], Subtraction)
