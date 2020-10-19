import pytest
import frogriverone

testdata = [(5, [1, 3, 1, 4, 2, 3, 5, 4], 6)]


@pytest.mark.parametrize("X,A,expected", testdata)
def test_frogriverone(X, A, expected):
    assert frogriverone.solution(X, A) == expected
