import pytest
import distinct

testdata = [([2, 1, 1, 2, 3, 1], 3), ([9, 9, 9, 9, 9], 1)]


@pytest.mark.parametrize("A,expected", testdata)
def test_distinct(A, expected):
    assert distinct.solution(A) == expected
