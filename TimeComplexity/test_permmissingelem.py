import pytest
import permmissingelem

testdata = [([2, 3, 1, 5], 4)]


@pytest.mark.parametrize("A,expected", testdata)
def test_permcheck(A, expected):
    assert permmissingelem.solution(A) == expected
