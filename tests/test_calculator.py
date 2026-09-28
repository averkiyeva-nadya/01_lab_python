import pytest

from toolkit.calculator import calculate
from toolkit.errors import (
    DivisionByZeroError,
    EmptyExpressionError,
    InvalidCharacterError,
    InvalidNumError,
    InvalidOperationError,
    MissedOperandError,
    TooManyDotsError,
    TwoBinaryOperatorsError,
)

#позитивные тесты

def test_addition():
    assert calculate('2+3') == 5

def test_subtraction():
    assert calculate("10-4") == 6


def test_multiplication():
    assert calculate("3*4") == 12


def test_division():
    assert calculate("10/4") == 2.5


def test_priority():
    assert calculate("2+3*4") == 14


def test_priority_with_two_operations():
    assert calculate("2*3+4") == 10


def test_negative_numbers():
    assert calculate("-2*-3") == 6

def test_unary_minus_after_plus():
    assert calculate("1+-2") == -1


def test_unary_minus_after_minus():
    assert calculate("1--2") == 3


def test_negative_number_at_start():
    assert calculate("-10+3") == -7


def test_spaces():
    assert calculate("10 / 4") == 2.5


def test_decimal_numbers():
    assert calculate("0.5+0.25") == 0.75


def test_many_operations():
    assert calculate("3+5*3+2") == 20


def test_division_left_to_right():
    assert calculate("20/5/2") == 2


def test_all_operations():
    assert calculate("10+6/2*3-4") == 15

#негативные тесты

def test_empty_expression():
    with pytest.raises(EmptyExpressionError):
        calculate('')

def test_missed_operand():
    with pytest.raises(MissedOperandError):
        calculate("1 2")

def test_only_spaces():
    with pytest.raises(EmptyExpressionError):
        calculate("   ")


def test_two_binary_operators():
    with pytest.raises(TwoBinaryOperatorsError):
        calculate("2*/3")


def test_invalid_character():
    with pytest.raises(InvalidCharacterError):
        calculate("2+a")

def test_division_by_zero():
    with pytest.raises(DivisionByZeroError):
        calculate("1/0")


def test_too_many_dots():
    with pytest.raises(TooManyDotsError):
        calculate("1.2.3")


def test_operator_at_end():
    with pytest.raises(InvalidOperationError):
        calculate("2+")


def test_multiplication_at_start():
    with pytest.raises(InvalidOperationError):
        calculate("*2")


def test_two_multiplications():
    with pytest.raises(TwoBinaryOperatorsError):
        calculate("2**3")

def test_two_divisions():
    with pytest.raises(TwoBinaryOperatorsError):
        calculate("2//3")


def test_plus_multiplication():
    with pytest.raises(TwoBinaryOperatorsError):
        calculate("2+*3")


def test_minus_multiplication():
    with pytest.raises(TwoBinaryOperatorsError):
        calculate("2-*3")


def test_invalid_symbol():
    with pytest.raises(InvalidNumError):
        calculate("2@3")

def test_invalid_letter():
    with pytest.raises(InvalidCharacterError):
        calculate('abc')

def test_numver_with_two_dots():
    with pytest.raises(TooManyDotsError):
        calculate('1.2.3+4')