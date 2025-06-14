import pytest
from neu import EvenOddChecker

@pytest.fixture
def even_odd_checker():
    return EvenOddChecker()

def test_is_even(even_odd_checker):
    assert even_odd_checker.is_even(0) == True
    assert even_odd_checker.is_even(-2) == True

def test_is_odd(even_odd_checker):
    assert even_odd_checker.is_odd(1) == True
    assert even_odd_checker.is_odd(-1) == True


