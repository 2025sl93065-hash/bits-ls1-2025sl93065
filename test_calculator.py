import pytest
from calculator import add, subtract, multiply, divide


# --- add tests ---

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 5) == 5


# --- subtract tests ---

def test_subtract_positive():
    assert subtract(10, 3) == 7

def test_subtract_negative():
    assert subtract(-1, -1) == 0

def test_subtract_zero():
    assert subtract(5, 0) == 5


# --- multiply tests ---

def test_multiply_positive():
    assert multiply(4, 5) == 20

def test_multiply_negative():
    assert multiply(-2, 3) == -6

def test_multiply_zero():
    assert multiply(7, 0) == 0


# --- divide tests ---

def test_divide_positive():
    assert divide(10, 2) == 5.0

def test_divide_negative():
    assert divide(-9, 3) == -3.0

def test_divide_fraction():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
