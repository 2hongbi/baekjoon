import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1

for a in arr:
    # 현재 수보다 num이 더 크면 그 수까지 push 연산
    while current <= a:
        stack.append(current)
        result.append("+")
        current += 1

    # 스택의 최상단이 num인 경우, pop 연산 수행
    if stack[-1] == a:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        break
else: # for 루프가 끝까지 실행되었을 때 else 블록 실행
    print("\n".join(result))