import pytest
from src.calculator import add, subtract, multiply, divide, power, modulo


# ──────────────────────────────────────────────
# Test add (Cộng)
# ──────────────────────────────────────────────
def test_add_two_positives():
    assert add(2, 3) == 5

def test_add_two_negatives():
    assert add(-1, -1) == -2

def test_add_positive_and_negative():
    assert add(-3, 5) == 2

def test_add_with_zero():
    assert add(0, 5) == 5

def test_add_floats():
    assert add(1.5, 2.5) == 4.0

def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000


# ──────────────────────────────────────────────
# Test subtract (Trừ)
# ──────────────────────────────────────────────
def test_subtract_positive_result():
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    assert subtract(3, 7) == -4

def test_subtract_same_numbers():
    assert subtract(5, 5) == 0

def test_subtract_with_zero():
    assert subtract(8, 0) == 8

def test_subtract_floats():
    assert subtract(5.5, 2.5) == 3.0


# ──────────────────────────────────────────────
# Test multiply (Nhân)
# ──────────────────────────────────────────────
def test_multiply_two_positives():
    assert multiply(3, 4) == 12

def test_multiply_with_zero():
    assert multiply(5, 0) == 0

def test_multiply_two_negatives():
    assert multiply(-2, -3) == 6

def test_multiply_positive_and_negative():
    assert multiply(-3, 4) == -12

def test_multiply_by_one():
    assert multiply(7, 1) == 7

def test_multiply_floats():
    assert multiply(2.5, 4.0) == 10.0


# ──────────────────────────────────────────────
# Test divide (Chia)
# ──────────────────────────────────────────────
def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_returns_float():
    result = divide(7, 2)
    assert result == 3.5

def test_divide_negative_dividend():
    assert divide(-9, 3) == -3.0

def test_divide_negative_divisor():
    assert divide(9, -3) == -3.0

def test_divide_both_negatives():
    assert divide(-8, -4) == 2.0

def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_divide_zero_by_number():
    assert divide(0, 5) == 0.0

def test_divide_by_zero_error_message():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(1, 0)


# ──────────────────────────────────────────────
# Test power (Lũy thừa)
# ──────────────────────────────────────────────
def test_power_positive_exp():
    assert power(2, 10) == 1024

def test_power_zero_exp():
    assert power(5, 0) == 1

def test_power_one_exp():
    assert power(7, 1) == 7

def test_power_negative_base():
    assert power(-2, 3) == -8

def test_power_negative_exp():
    assert power(2, -1) == 0.5

def test_power_zero_base():
    assert power(0, 5) == 0


# ──────────────────────────────────────────────
# Test modulo (Chia lấy dư)
# ──────────────────────────────────────────────
def test_modulo_normal():
    assert modulo(10, 3) == 1

def test_modulo_exact_division():
    assert modulo(9, 3) == 0

def test_modulo_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        modulo(5, 0)

def test_modulo_larger_divisor():
    assert modulo(3, 10) == 3
