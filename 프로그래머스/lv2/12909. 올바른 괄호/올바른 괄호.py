def solution(s):
    stack = []
    s = list(s)
    for i in s:
        stack.append(i)
        if i == ')':
            if len(stack) == 1:
                return False
            elif stack[-2] == '(':
                stack.pop(-2)
                stack.pop(-1)
    return len(stack) == 0