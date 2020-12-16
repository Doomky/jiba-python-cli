from tokens import Token
from tokens.token_parser import TokenParser
from tokens.rpn_transformer import RpnTransformer
from tokens.token_queue import TokenQueue
from tokens.rpn_calculator import RpnCalculator
from tokens.number import Number


def test_global1():
    calculation_str = "(3 + 8) * (5/2) - 1"

    token_list: [Token] = TokenParser(calculation_str).parse()

    token_queue: TokenQueue = RpnTransformer(token_list).transform()

    number: Number = RpnCalculator(token_queue).compute()

    assert str(number) == "21"
