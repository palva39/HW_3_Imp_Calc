'''My Calculator Test'''
import pytest
from calculator import Calculator

def test_addition():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, -1) == -2

def test_subtraction():
    assert Calculator.subtract(2, 3) == -1
    assert Calculator.subtract(-1, -1) == 0

def test_multiplication():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-1, -1) == 1

def test_division():
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(-1, -1) == 1

def test_divide_by_zero_exception():
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)

def test_last_calculation():
    Calculator.add(5, 7)
    assert Calculator.last_calculation() == (5, 7, '+', 12)

@pytest.fixture
def clean_history():
    Calculator.history.clear()

def test_history(clean_history):
    Calculator.add(2, 2)
    assert Calculator.last_calculation() == (2, 2, '+', 4)
    Calculator.subtract(3, 2)
    assert Calculator.last_calculation() == (3, 2, '-', 1)
