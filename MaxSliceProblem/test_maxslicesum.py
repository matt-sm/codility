import pytest
import maxslicesum

testdata = [([3, 2, -6, 4, 0], 5)]


@pytest.mark.parametrize("A,expected", testdata)
def test_maxslicesum(A, expected):
    assert maxslicesum.solution(A) == expected
