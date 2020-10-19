def solution(A):
    current = 0
    best = float("-inf")

    for n in A:
        current = max(n, current + n)
        best = max(best, current)
    return best
