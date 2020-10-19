import pytest
import passingcars

testdata = [([0, 1, 0, 1, 1], 5)]


@pytest.mark.parametrize("A,expected", testdata)
def test_passingcars(A, expected):
    assert passingcars.solution(A) == expected
