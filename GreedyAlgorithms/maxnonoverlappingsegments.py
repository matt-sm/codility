def solution(A, B):
    if len(A) <= 1:
        return len(A)

    result = 1
    end = 0

    for i in range(1, len(A)):
        if A[i] > B[end]:
            result += 1
        end = i

    return result
