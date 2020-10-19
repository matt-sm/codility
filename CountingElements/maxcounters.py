def solution(N, A):
    counters = [0 for _ in range(N)]
    max_counter = 0
    current_max = 0

    for x in A:
        if x <= N:
            counters[x - 1] = max(counters[x - 1], max_counter) + 1
            current_max = max(counters[x - 1], current_max)
        else:
            max_counter = current_max

    return [max(max_counter, x) for x in counters]

