import pytest

from app.main import get_coin_combination


# @pytest.mark.parametrize(
#
# )
def test_should_return_pennies() -> None:
    assert get_coin_combination(1) == [1, 0, 0, 0]


def test_should_return_one_nickels() -> None:
    assert get_coin_combination(6) == [1, 1, 0, 0]


def test_should_return_one_dimes() -> None:
    assert get_coin_combination(17) == [2, 1, 1, 0]


def test_should_return_one_quarters() -> None:
    assert get_coin_combination(50) == [0, 0, 0, 2]


# def test_should_return_value_error_if_negative() -> None:
#     assert get_coin_combination(-1) == ValueError
