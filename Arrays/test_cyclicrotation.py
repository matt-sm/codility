import pytest
import cyclicrotation

testdata = [([3, 8, 9, 7, 6], 3, [9, 7, 6, 3, 8]), ([0, 0, 0], 1, [0, 0, 0]), ([1, 2, 3, 4], 4, [1, 2, 3, 4])]


@pytest.mark.parametrize("A,K,expected", testdata)
def test_cyclicrotation(A, K, expected):
    assert cyclicrotation.solution(A, K) == expected
