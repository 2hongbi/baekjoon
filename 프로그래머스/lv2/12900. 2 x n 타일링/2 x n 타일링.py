def solution(n):
    tiles = [0 for _ in range(n)]
    tiles[0], tiles[1] = 1, 2
    for i in range(2, n):
        tiles[i] = (tiles[i - 1] + tiles[i - 2]) % 1000000007
    return tiles[n - 1]