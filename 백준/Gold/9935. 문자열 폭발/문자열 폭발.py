import sys

input = sys.stdin.readline

orig_str = input().strip()
bomb_str = input().strip()
bomb_len = len(bomb_str)

stack = []

for char in orig_str:
    stack.append(char)

    # 폭발 문자열 확인 :
    # 1. 매번 마지막에 추가된 문자열이 폭발 문자열과 일치하는지 확인
    # 2. 문자열 확인 시 폭발 문자열의 길이만큼 확인
    if len(stack) >= bomb_len and ''.join(stack[-bomb_len:]) == bomb_str:
        del stack[-bomb_len:]


print(''.join(stack)) if stack else print('FRULA')