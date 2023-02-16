import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
deque = deque()
A = list(map(int, input().split()))

for i in range(N):
    while deque and deque[-1][0] > A[i]:
        deque.pop()
    deque.append((A[i], i))
    if deque[0][1] <= i - L:  # 범위에서 벗어난 값은 덱에서 제거
        deque.popleft()
    print(deque[0][0], end=' ')