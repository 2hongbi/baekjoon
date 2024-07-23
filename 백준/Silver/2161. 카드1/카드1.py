# https://www.acmicpc.net/problem/2161
# N장의 카드가 있음. 각각의 카드는 1~N 번호 붙음. 1번이 제일 위에, N번이 가장 아래
# 1. 제일 위의 카드 버림
# 2. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김
# n=4일 때, 1234 -> 1 버림 -> 234 남음 -> 2 제일 아래로 옮김 -> 342 -> 3 버림 -> 4 제일 아래로 옮김 -> 2 만 남음
# N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드 출력
import sys

n = int(sys.stdin.readline())
cards = [i for i in range(1, n + 1)]

discard = []

while len(cards) > 1:
    discard.append(cards.pop(0))
    cards.append(cards.pop(0))

print(*discard, *cards)