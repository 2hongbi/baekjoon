import sys
import itertools
input = sys.stdin.readline

dwarfs = [int(input()) for _ in range(9)]

# 순열 : itertools.permutations, 조합: itertools.combinations
for i in itertools.combinations(dwarfs, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break