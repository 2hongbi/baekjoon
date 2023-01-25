def solution(numbers):
    numbers.sort()
    a, b = numbers[0] * numbers[1], numbers[-1] * numbers[-2]
    if a > b:
        return a
    return b