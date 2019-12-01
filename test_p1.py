import pytest

from p1 import rocket_fuel, rocket_fuel_recursive


@pytest.mark.parametrize("test_input,expected", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
def test_rocket_fuel(test_input, expected):
    assert rocket_fuel(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(14, 2), (1969, 966), (100756, 50346)])
def test_rocket_fuel_recursive(test_input, expected):
    assert rocket_fuel_recursive(test_input) == expected