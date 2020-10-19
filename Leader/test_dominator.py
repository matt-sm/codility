import pytest
import dominator

testdata = [([3, 4, 3, 2, 3, -1, 3, 3], 0), ([0, 0, 1, 1, 1], 2), ([2, 1, 3, 4, -1, 2, 9], -1)]


@pytest.mark.parametrize("A,expected", testdata)
def test_dominator(A, expected):
    assert dominator.solution(A) == expected
