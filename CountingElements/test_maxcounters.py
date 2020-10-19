import pytest
import maxcounters

testdata = [(5, [3, 4, 4, 6, 1, 4, 4], [3, 2, 2, 4, 2]), (2, [4, 4], [0, 0])]


@pytest.mark.parametrize("N,A,expected", testdata)
def test_example(N, A, expected):
    assert maxcounters.solution(N, A) == expected
