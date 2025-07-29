from app.app import Calculator
from decimal import Decimal

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

"""
Test the pi function
"""
def test_pi():
    assert Decimal(Calculator.pi()) == Decimal(3.141592653589793238)
    
"""
Test the golden function
"""
def test_golden():
    assert Decimal(Calculator.golden()) == Decimal(1.618033988749)
    
"""
Test the goldenpi function
"""
def test_goldenpi():
    assert Decimal(Calculator.goldenpi()) == Decimal(3.141592653589793238 * 1.618033988749)

"""
Test the square function
"""
@pytest.mark.parametrize("a, b", [
    (1, 1),
    (2, 4),
    (3, 9)
])
def test_square(a, b):
    assert Calculator.square(a) == b