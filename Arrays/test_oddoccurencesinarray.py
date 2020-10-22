import pytest
import oddoccurencesinarray

testdata = [([9, 3, 9, 3, 9, 7, 9], 7)]


@pytest.mark.parametrize("A,expected", testdata)
def test_oddoccurencesinarray(A, expected):
    assert oddoccurencesinarray.solution(A) == expected
