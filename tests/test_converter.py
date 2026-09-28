import pytest

from toolkit.converter import converter
from toolkit.errors import (
    InvalidMeasureError,
    InvalidValueError,
    UncompletableMeasuresError,
)

#положительные тесты

def test_mm_to_m():
    assert converter(1000, "mm", "m") == 1


def test_m_to_mm():
    assert converter(1, "m", "mm") == 1000


def test_cm_to_m():
    assert converter(100, "cm", "m") == 1


def test_m_to_cm():
    assert converter(2, "m", "cm") == 200


def test_km_to_m():
    assert converter(1, "km", "m") == 1000


def test_km_to_cm():
    assert converter(1, "km", "cm") == 100000


def test_g_to_kg():
    assert converter(500, "g", "kg") == 0.5


def test_kg_to_g():
    assert converter(1.5, "kg", "g") == 1500


def test_c_to_f():
    assert converter(0, "c", "f") == 32


def test_f_to_c():
    assert converter(32, "f", "c") == 0


def test_c_to_k():
    assert converter(0, "c", "k") == pytest.approx(273.15)


def test_k_to_c():
    assert converter(273.15, "k", "c") == pytest.approx(0)


def test_absolute_zero():
    assert converter(-273.15, "c", "k") == pytest.approx(0)


def test_uppercase_units():
    assert converter(1000, "MM", "M") == 1


def test_same_units():
    assert converter(15, "kg", "kg") == 15


#негативные тесты

def test_below_absolute_zero_celsius():
    with pytest.raises(InvalidValueError):
        converter(-274, "c", "k")


def test_below_absolute_zero_kelvin():
    with pytest.raises(InvalidValueError):
        converter(-1, "k", "c")


def test_below_absolute_zero_fahrenheit():
    with pytest.raises(InvalidValueError):
        converter(-500, "f", "c")


def test_mass_to_length():
    with pytest.raises(UncompletableMeasuresError):
        converter(1, "kg", "m")


def test_length_to_mass():
    with pytest.raises(UncompletableMeasuresError):
        converter(1, "m", "kg")


def test_temperature_to_length():
    with pytest.raises(UncompletableMeasuresError):
        converter(1, "c", "m")


def test_length_to_temperature():
    with pytest.raises(UncompletableMeasuresError):
        converter(1, "m", "c")


def test_mass_to_temperature():
    with pytest.raises(UncompletableMeasuresError):
        converter(1, "kg", "c")


def test_invalid_start_unit():
    with pytest.raises(InvalidMeasureError):
        converter(1, "abc", "m")


def test_invalid_end_unit():
    with pytest.raises(InvalidMeasureError):
        converter(1, "m", "abc")


def test_invalid_both_units():
    with pytest.raises(InvalidMeasureError):
        converter(1, "abc", "xyz")


def test_unknown_mass_unit():
    with pytest.raises(InvalidMeasureError):
        converter(1, "lb", "kg")


def test_unknown_temperature_unit():
    with pytest.raises(InvalidMeasureError):
        converter(1, "celsius", "k")

