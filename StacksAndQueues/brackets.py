from collections import deque


def solution(S):
    d = deque()
    brackets = {"{": "}", "[": "]", "(": ")"}

    for c in S:
        if c in brackets.keys():
            d.append(c)
        else:
            if len(d) == 0:
                return 0
            b = d.pop()
            if brackets[b] != c:
                return 0

    return 1 if len(d) == 0 else 0
