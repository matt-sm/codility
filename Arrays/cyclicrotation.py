def solution(A, K):
    result = [0 for _ in range(len(A))]

    for i in range(len(A)):
        j = (i + K) % len(A)
        result[j] = A[i]

    return result
