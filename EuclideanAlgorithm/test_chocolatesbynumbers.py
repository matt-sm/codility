import pytest
import chocolatesbynumbers

testdata = [(10, 4, 5), (24, 18, 4), ((3 ** 9) * (2 ** 14), (2 ** 14) * (2 ** 14), 19683)]


@pytest.mark.parametrize("N,M,expected", testdata)
def test_chocolatesbynumbers(N, M, expected):
    assert chocolatesbynumbers.solution(N, M) == expected
