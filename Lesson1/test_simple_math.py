import pytest
from simple_math import SimpleMath

@pytest.fixture
def simple_math():
    return SimpleMath()

def test_square_positive(simple_math):
    assert simple_math.square(2) == 4
    assert simple_math.square(5) == 25

def test_square_negative(simple_math):
    assert simple_math.square(-2) == 4
    assert simple_math.square(-5) == 25

def test_square_zero(simple_math):
    assert simple_math.square(0) == 0

def test_cube_positive(simple_math):
    assert simple_math.cube(2) == 8
    assert simple_math.cube(3) == 27

def test_cube_negative(simple_math):
    assert simple_math.cube(-3) == -27
    assert simple_math.cube(-2) == -8

def test_cube_zero(simple_math):
    assert simple_math.cube(0) == 0
