from .errors import (
    EmptyExpressionError,
    InvalidCharacterError,
    InvalidNumError,
    MissedOperandError,
    TooManyDotsError,
    )


def tokenize_fsm(expr):

    for i in range(1, len(expr)-1):
        if (
            expr[i] == ' '
            and (expr[i-1].isdigit() or expr[i-1] == '.')
            and (expr[i+1].isdigit() or expr[i+1] == '.')
        ):
            raise MissedOperandError("Невозможно обработать пропущенный операнд")

    expr = str(expr).replace(' ', '')

    tokens = []
    state = 'START'
    current_token = ''
    has_dot = False

    if not expr:
        raise EmptyExpressionError("Невозможно обработать пустое выражение")
    
    for char in expr:
        if state == 'START':
            if char.isdigit():
                state = 'NUMBER'
                current_token = char
                has_dot = False

            elif char in ['+', '-', '*', '/']:
                tokens.append(('OPERATOR', char))
            else:
                raise InvalidCharacterError(char)


        elif state == 'NUMBER':
            if char.isdigit():
                current_token += char

            elif char == '.':
                if has_dot:
                    raise TooManyDotsError("Невозможно обработать число с несколькими точками")

                current_token += '.'
                has_dot = True

            elif char in ['+', '-', '*', '/']:
                if current_token[-1] == '.':
                    raise InvalidNumError()
                else:
                    tokens.append(('NUMBER', float(current_token)))
                tokens.append(('OPERATOR', char))
                current_token = ''
                state = 'START'

            else:
                raise InvalidNumError()
    if current_token and current_token[-1] == '.':
            raise InvalidNumError()
    
    if state == 'NUMBER':
        tokens.append(('NUMBER', float(current_token)))

    return tokens