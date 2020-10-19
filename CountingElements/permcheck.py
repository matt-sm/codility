def solution(A):
    s = set()
    for n in A:
        s.add(n)

    return int(len(s) == max(A) and len(s) == len(A))
