from typing import List

from . import Token, Number, Operator
from .parenthesis import Parenthesis, ParenthesisType
from .token_queue import TokenQueue


class RpnTransformer:

    def __init__(self, token_list: List[Token]):
        self.token_list: List[Token] = token_list

    def transform(self) -> TokenQueue:
        token_list_copy = self.token_list.copy()
        token_queue = TokenQueue()
        operator_stack = []
        while token_list_copy:
            token = token_list_copy.pop(0)
            if type(token) == Number:
                token_queue.put(token)
            elif isinstance(token, Operator):
                while (len(operator_stack) > 0 and
                       (operator_stack[-1].precedence > token.precedence or (operator_stack[-1].precedence == token.precedence and token.associativity is False)) and
                       (type(operator_stack[-1]) != Parenthesis or operator_stack[-1].get_type() != ParenthesisType.left)):
                    token_queue.put(operator_stack.pop())
                operator_stack.append(token)
            elif type(token) == Parenthesis and token.get_type() == ParenthesisType.left:
                operator_stack.append(token)
            elif type(token) == Parenthesis and token.get_type() == ParenthesisType.right:
                while len(operator_stack) > 0 and (type(operator_stack[-1]) != Parenthesis or operator_stack[-1].get_type() != ParenthesisType.left):
                    token_queue.put(operator_stack.pop())
                if len(operator_stack) == 0:
                    raise Exception("Mismatched parenthesis")

                if len(operator_stack) > 0 and type(operator_stack[-1]) == Parenthesis and operator_stack[-1].get_type() == ParenthesisType.left:
                    operator_stack.pop()
                if len(operator_stack) > 0 and isinstance(operator_stack[-1], Operator):
                    token_queue.put(operator_stack.pop())

        while len(operator_stack) > 0:
            operator = operator_stack.pop()
            if type(operator) == Parenthesis:
                raise Exception("Mismatched parenthesis")
            token_queue.put(operator)

        return token_queue
