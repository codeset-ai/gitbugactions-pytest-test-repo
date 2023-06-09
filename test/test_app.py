from app.app import Calculator

import pytest

"""
Test the sumInt function
"""
@pytest.mark.parametrize("a, b, c", [
    (1, 1, 2),
    (1, 2, 3),
    (1, -1, 0)
])
def test_sumInt(a, b, c):
    assert Calculator.sumInt(a, b) == c
    
"""
Test the sumFloat function
"""
@pytest.mark.parametrize("a, b, c", [
    (1.0, 1.0, 2.0),
    (1.0, 2.0, 3.0),
    (1.0, -1.0, 0.0)
])
def test_sumFloat(a, b, c):
    assert Calculator.sumFloat(a, b) == c

"""
Test the sum function
"""
@pytest.mark.parametrize("a, b, c", [
    (1, 1, 2),
    (1, 2, 3),
    (1, -1, 0),
    (1.0, 1.0, 2.0),
    (1.0, 2.0, 3.0),
    (1.0, -1.0, 0.0)
])
def test_sum(a, b, c):
    assert Calculator.sum(a, b) == c
