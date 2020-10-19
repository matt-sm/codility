import pytest
import binarygap

testdata = [(1041, 5), (32, 0), (15, 0), (6291457, 20), (328, 2)]


@pytest.mark.parametrize("N,expected", testdata)
def test_binarygap(N, expected):
    assert binarygap.solution(N) == expected
