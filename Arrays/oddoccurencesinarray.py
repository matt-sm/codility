from collections import Counter


def solution(A):
    c = Counter(A)
    for key, value in c.items():
        if value % 2 != 0:
            return key
