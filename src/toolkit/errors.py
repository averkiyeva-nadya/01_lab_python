class ProjectErrors(Exception):
    pass

class Calculator(ProjectErrors):
    pass

class EmptyExpressionError(Calculator):
    def __init__(self, message: str = 'Невозможно обработать пустое выражение'):
        super().__init__(message)

class InvalidCharacterError(Calculator):
    def __init__(self, char):
        self.char = char
        super().__init__(f'Недопустимый символ {char}')

class MissedOperandError(Calculator):
    def __init__(self, message: str='Невозможно обработать пропущенный операнд'):
        super().__init__(message)

class TwoBinaryOperatorsError(Calculator):
    def __init__(self, message: str='Невозможно обработать два бинарных оператора подряд'):
        super().__init__(message)

class DivisionByZeroError(Calculator):
    def __init__(self, message: str='Нельзя делить на 0'):
        super().__init__(message)

class TooManyDotsError(Calculator):
    def __init__(self, message: str='Невозможно обработать число с несколькими точками'):
        super().__init__(message)

class InvalidNumError(Calculator):
    def __init__(self, message: str='Некорректное число'):
        super().__init__(message)

class InvalidOperationError(Calculator):
    def __init__(self, message: str='Недопустимая операция'):
        super().__init__(message)

class Converter(ProjectErrors):
    pass    

class InvalidMeasureError(Converter):
    def __init__(self, message: str='Недопустимая единица измерения'):
        super().__init__(message)

class UncompletableMeasuresError(Converter):
    def __init__(self, message: str='Невозможно преобразовать данные единицы измерения'):
        super().__init__(message)

class InvalidValueError(Converter):
    def __init__(self, message: str='Недопустимое значение'):
        super().__init__(message)