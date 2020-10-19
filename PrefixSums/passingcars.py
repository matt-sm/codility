def solution(A):
    result = 0
    east_cars = 0

    for car in A:
        if car == 0:
            east_cars += 1
        if east_cars > 0:
            if car == 1:
                result += east_cars
                if result > 1000000000:
                    return -1
    return result
