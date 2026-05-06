import pytest
from src.math_utils import divide

def test_divide_normal():
    assert divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(8, 0)
