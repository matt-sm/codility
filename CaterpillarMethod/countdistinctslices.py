def solution(M, A):
    the_sum = 0
    front = back = 0
    seen = set()
    while front < len(A) and back < len(A):
        while front < len(A) and A[front] not in seen:
            the_sum += front - back + 1
            seen.add(A[front])
            front += 1
        else:
            while front < len(A) and back < len(A) and A[back] != A[front]:
                seen.remove(A[back])
                back += 1

            seen.remove(A[back])
            back += 1

    return min(the_sum, 1000000000)

