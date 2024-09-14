n = int(input())

def is_vps(string):
    stack = []
    for st in string:
        if st == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                continue
        stack.append(st)

    if stack:
        return False
    return True


for _ in range(n):
    print('YES') if is_vps(input()) else print('NO')