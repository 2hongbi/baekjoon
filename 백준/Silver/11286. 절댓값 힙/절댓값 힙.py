import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x != 0: # 0이면 출력
        heapq.heappush(heap, (abs(x), x))  # 절댓값, 원래값 저장
    else:
        if heap:
            print(heapq.heappop(heap)[1]) # 절댓값이 가장 작은값 제거 및 출력
        else:
            print(0)