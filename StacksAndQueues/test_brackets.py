import pytest
import brackets

testdata = [("{[()()]}", 1), ("([)()]", 0), ("((((", 0)]


@pytest.mark.parametrize("S,expected", testdata)
def test_backets(S, expected):
    assert brackets.solution(S) == expected
