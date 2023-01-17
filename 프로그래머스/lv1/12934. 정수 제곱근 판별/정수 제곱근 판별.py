def solution(n):
    dividor = int(n ** (1 / 2))
    if n / dividor == dividor:
        return (dividor + 1) ** 2
    else:
        return -1