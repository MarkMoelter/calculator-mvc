import src.calc_captions as cc
from src.models import Model


def test_calculate_input_C_clears_value():
    model = Model()

    model.value = "0"
    model.calculate(cc.CLEAR)
    assert model.value == ""


def test_calculate_input_INVERT_inverts_value():
    model = Model()

    model.value = "1"

    assert model.calculate(cc.INVERT) == "-1"


def test_calculate_input_INVERT_int_value_stays_int():
    model = Model()

    model.value = "1"

    assert "." not in model.calculate(cc.INVERT)


def test_calculate_input_INVERT_float_value_stays_float():
    model = Model()

    model.value = "1.0"

    assert "." in model.calculate(cc.INVERT)
