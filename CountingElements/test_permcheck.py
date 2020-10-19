import pytest
import permcheck

testdata = [([4, 1, 3, 2], 1), ([4, 1, 3], 0)]


@pytest.mark.parametrize("A,expected", testdata)
def test_permcheck(A, expected):
    assert permcheck.solution(A) == expected
