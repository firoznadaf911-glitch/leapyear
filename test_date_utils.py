# test_date_utils.py
import pytest
from date_utils import is_leap, days_in_month, day_of_year, days_remaining_in_year

def test_is_leap_standard():
    assert is_leap(2024) is True
    assert is_leap(2025) is False

def test_is_leap_century_rules():
    assert is_leap(2000) is True   # Divisible by 400 -> leap
    assert is_leap(1900) is False  # Divisible by 100 but not 400 -> not leap

def test_days_in_month_february():
    assert days_in_month(2, 2024) == 29
    assert days_in_month(2, 2025) == 28

def test_days_in_month_standard():
    assert days_in_month(1, 2025) == 31
    assert days_in_month(4, 2025) == 30

def test_day_of_year_leap_and_common():
    assert day_of_year(15, 3, 2024) == 75   # 31 + 29 + 15
    assert day_of_year(15, 3, 2025) == 74   # 31 + 28 + 15
    assert day_of_year(31, 12, 2024) == 366

def test_days_remaining_in_year():
    assert days_remaining_in_year(31, 12, 2024) == 0
    assert days_remaining_in_year(1, 1, 2025) == 364

def test_invalid_inputs():
    with pytest.raises(ValueError):
        days_in_month(13, 2025)
    with pytest.raises(ValueError):
        day_of_year(29, 2, 2025)
