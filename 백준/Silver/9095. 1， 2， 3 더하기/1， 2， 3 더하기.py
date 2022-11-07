import sys

input = sys.stdin.readline

ans = [0] * 11  # 입력받은 정수는 11 미만이므로
ans[1] = 1
ans[2] = 2
ans[3] = 4

for i in range(4, 11):
    ans[i] = sum(ans[i-3:i])

T = int(input())
for _ in range(T):
    print(ans[int(input())])