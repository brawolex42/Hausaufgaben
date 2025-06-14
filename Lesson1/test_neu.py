import pytest
from neu import EvenOddChecker

@pytest.fixture
def even_odd_checker():
    return EvenOddChecker()

def test_is_even(even_odd_checker):
    assert even_odd_checker.is_even(0) is True
    assert even_odd_checker.is_even(2) is True
    assert even_odd_checker.is_even(-2) is True
    assert even_odd_checker.is_even(1) is False
    assert even_odd_checker.is_even(-1) is False

def test_is_odd(even_odd_checker):
    assert even_odd_checker.is_odd(1) is True
    assert even_odd_checker.is_odd(-1) is True
    assert even_odd_checker.is_odd(2) is False
    assert even_odd_checker.is_odd(-2) is False
    assert even_odd_checker.is_odd(0) is False
