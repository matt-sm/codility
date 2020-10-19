def solution(N):
    b = "{0:b}".format(N)
    gap = 0
    result = 0

    for n in b:
        if n == "0":
            gap += 1
        if n == "1":
            if gap > result:
                result = gap
            gap = 0

    return result
