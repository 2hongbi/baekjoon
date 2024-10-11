import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')

people = [i for i in range(n)]
for start_team in combinations(people, n // 2):
    # print(start_team)
    link_team = [i for i in people if i not in start_team]

    start_score = 0
    for i in start_team:
        for j in start_team:
            if i != j:
                start_score += s[i][j]

    link_score = 0
    for i in link_team:
        for j in link_team:
            if i != j:
                link_score += s[i][j]

    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)

print(min_diff)