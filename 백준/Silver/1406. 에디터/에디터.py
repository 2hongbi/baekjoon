import sys
input = sys.stdin.readline

left_stack = list(input().strip())  # 커서 왼쪽의 문자들
right_stack = [] # 커서 오른쪽의 문자들

m = int(input())

for _ in range(m):
    cmd = input().split()

    if cmd[0] == "L":
        if left_stack:
            right_stack.append(left_stack.pop())
    elif cmd[0] == "D":
        if right_stack:
            left_stack.append(right_stack.pop())
    elif cmd[0] == "B": # 커서 왼쪽에 있는 문자 삭제
        if left_stack:
            left_stack.pop()
    elif cmd[0] == "P":
        left_stack.append(cmd[1])


print("".join(left_stack + right_stack[::-1]))