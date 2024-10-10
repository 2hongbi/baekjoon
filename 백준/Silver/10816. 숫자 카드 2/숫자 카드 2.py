import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

card_dict = defaultdict(int)
for card in cards:
    card_dict[card] += 1

m = int(input())
targets = list(map(int, input().split()))
answer = []
for target in targets:
    answer.append(card_dict.get(target, 0))

print(*answer)