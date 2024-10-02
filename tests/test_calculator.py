'''My Calculator Test'''
import pytest
from calculator import Calculator

def test_addition():
    '''Tests the addition function'''
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, -1) == -2

def test_subtraction():
    '''Tests the subtraction function'''
    assert Calculator.subtract(2, 3) == -1
    assert Calculator.subtract(-1, -1) == 0

def test_multiplication():
    '''Tests that multiplcation function'''
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-1, -1) == 1

def test_division():
    '''Tests the division function'''
    assert Calculator.divide(10, 2) == 5
    assert Calculator.divide(-1, -1) == 1

def test_divide_by_zero_exception():
    '''Tests the addition function when diveded by 0'''
    with pytest.raises(ValueError):
        Calculator.divide(10, 0)

def test_last_calculation():
    '''Tests the last calculation done function'''
    Calculator.add(5, 7)
    assert Calculator.last_calculation() == (5, 7, '+', 12)

@pytest.fixture
def clean_history(): # pylint: disable=redefined-outer-name
    '''Tests the clean history'''
    Calculator.history.clear()

def test_history(clean_history): # pylint: disable=unused-argument
    '''Test the calculation history functionality.'''
    Calculator.add(2, 2)
    assert Calculator.last_calculation() == (2, 2, '+', 4)
    Calculator.subtract(3, 2)
    assert Calculator.last_calculation() == (3, 2, '-', 1)
