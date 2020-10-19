def solution(A):
    current_candidate = 0
    counter = 0

    for e in A:
        if counter == 0:
            current_candidate = e
            counter = 1
        else:
            if e == current_candidate:
                counter += 1
            else:
                counter -= 1

    count = A.count(current_candidate)

    if count > len(A) // 2:
        return A.index(current_candidate)

    return -1
