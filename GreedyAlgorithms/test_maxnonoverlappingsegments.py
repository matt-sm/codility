import pytest
import maxnonoverlappingsegments

testdata = [([1, 3, 7, 9, 9], [5, 6, 8, 9, 10], 3)]


@pytest.mark.parametrize("A,B,expected", testdata)
def test_maxnonoverlappingsegments(A, B, expected):
    assert maxnonoverlappingsegments.solution(A, B) == expected
