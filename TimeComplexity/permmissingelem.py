def solution(A):
    n = len(A) + 1
    result = n * (n + 1) // 2
    return result - sum(A)
