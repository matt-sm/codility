import pytest
import countdistinctslices

testdata = [(5, [3, 4, 5, 5, 2], 9)]


@pytest.mark.parametrize("M,A,expected", testdata)
def test_countdistinctslices(M, A, expected):
    assert countdistinctslices.solution(M, A) == expected
