import src.calc_captions as cc
from src.models import Model


def test_calculate_input_CLEAR_clears_value():
    model = Model()

    model.value = "01234"
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


def test_calculate_input_DECIMAL_adds_decimal_point_at_end():
    model = Model()

    model.value = "1"

    assert model.calculate(cc.DECIMAL) == "1."


def test_calculate_input_DECIMAL_does_not_add_two_decimals():
    model = Model()

    model.value = "1"

    model.calculate(cc.DECIMAL)
    assert model.value == "1."

    model.calculate(cc.DECIMAL)
    assert model.value == "1."


def test_calculate_input_DELETE_removes_last_digit():
    model = Model()

    model.value = "1234"

    assert model.calculate(cc.DELETE) == "123"


def test_calculate_input_DELETE_removes_decimal_at_end():
    model = Model()

    model.value = "123."

    assert model.calculate(cc.DELETE) == "123"


def test_calculate_input_1_appends_to_value():
    model = Model()

    assert model.calculate("1") == "1"
