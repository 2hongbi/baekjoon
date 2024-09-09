import sys
from collections import deque

input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))

queue = deque() # 슬라이딩 윈도우에서 최소값의 인덱스를 저장하는 덱

for i in range(n):
    # 현재 값보다 큰 값들은 덱에서 제거
    while queue and a[queue[-1]] > a[i]:
        queue.pop() # 오른쪽 끝의 요소 제거

    queue.append(i) # 현재 인덱스를 덱에 추가

    if queue[0] <= i - l:
        queue.popleft() # 왼쪽 끝의 요소 제거

    print(a[queue[0]], end=' ')