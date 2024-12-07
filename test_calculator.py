import pytest
from calculator import Calculator

def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0
    assert Calculator.add(0, 0) == 0

def test_subtract():
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(0, 0) == 0
    assert Calculator.subtract(-1, -1) == 0

def test_multiply():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-1, 1) == -1
    assert Calculator.multiply(0, 100) == 0

def test_divide():
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(3, 1) == 3
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)
