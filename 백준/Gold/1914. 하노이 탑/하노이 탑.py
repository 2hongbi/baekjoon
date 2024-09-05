import sys
input = sys.stdin.readline

def hanoi(n, start='1', mid='2', end='3'):
    if n == 1:
        print(f"{start} {end}")
    else:
        # 1. n-1개의 원반을 시작 기둥에서 보조 기둥으로 옮기기
        hanoi(n-1, start, end, mid)
        # 2. 가장 큰 원반을 시작 기둥에서 목표 기둥으로 옮기기
        print(f"{start} {end}")
        # 3. n-1개의 원반을 보조 기둥에서 목표 기둥으로 옮기기
        hanoi(n-1, mid, start, end)


n = int(input())
print(2**n - 1) # 이동횟수는 항상 2^n - 1
if n <= 20:
    hanoi(n)