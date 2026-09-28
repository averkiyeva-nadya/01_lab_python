from .errors import (
    DivisionByZeroError,
    EmptyExpressionError,
    InvalidOperationError,
    TwoBinaryOperatorsError,
)
from .tokenization import tokenize_fsm


def validation(tokens):

    if not tokens:
        raise EmptyExpressionError()

    if len(tokens) > 1 and tokens[0][1] in ['+', '-'] and tokens[1][1] in ['+', '-']:
        raise InvalidOperationError()
    
    if tokens[0][0] == 'OPERATOR' and tokens[0][1] in ['+', '-']:
        pass
    elif tokens[0][0] == 'OPERATOR':
        raise InvalidOperationError()

    if tokens[-1][0] == 'OPERATOR':
        raise InvalidOperationError()
    
    for i in range(len(tokens)-1):
        if tokens[i][0] == 'OPERATOR' and tokens[i+1][0] == 'OPERATOR':
            if tokens[i][1] in ['+', '-'] and tokens[i+1][1] in ['+', '-']:
                if i + 2 >= len(tokens) or tokens[i + 2][0] == 'OPERATOR':
                    raise InvalidOperationError()
            elif tokens[i][1]+tokens[i+1][1] in ['**', '//', '+*', '+/', '-*', '-/', '*/', '/*']:
                raise TwoBinaryOperatorsError()
            
    return tokens


def addunaroperator(tokens):
    f = True
    l = [['OPERATOR', 1]]
    rez = []
    for typee, val in tokens:
        if typee==l[-1][0] == 'OPERATOR':
            f = (val == '+')
        elif typee == 'NUMBER':
            if not f:
                val = -val
            rez.append([typee, val])
            f = True
        else:
            rez.append([typee, val])
            f = True
        l.append([typee, val])
        
    return rez

class Stack:

    def __init__(self, *args):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


def to_rpn(tokens):
    output = []
    operators = Stack()

    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    for typee, val in tokens:

        if typee == 'NUMBER':
            output.append(('NUMBER', val))

        else:
            while (
                not operators.is_empty()
                and priority[operators.items[-1][1]] >= priority[val]
            ):
                output.append(operators.pop())

            operators.push(('OPERATOR', val))

    while not operators.is_empty():
        output.append(operators.pop())

    return output


def calculate_rpn(rpn):
    stack = Stack()

    for typee, val in rpn:

        if typee == 'NUMBER':
            stack.push(val)

        else:
            right = stack.pop()
            left = stack.pop()

            if val == '+':
                result = left + right

            elif val == '-':
                result = left - right

            elif val == '*':
                result = left * right

            elif val == '/':
                if right == 0:
                    raise DivisionByZeroError()
                result = left / right

            stack.push(result)

    return stack.pop()


def calculate(expr):
    tokens = tokenize_fsm(expr)
    tokens = validation(tokens)
    tokens = addunaroperator(tokens)
    rpn = to_rpn(tokens)
    result = calculate_rpn(rpn)

    result = round(result, 10)

    if result.is_integer():
        return int(result)

    return result


