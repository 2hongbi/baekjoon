def check_bracket(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
    return False if len(stack) else True

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        if check_bracket(s):
            answer += 1
        s = s[1:] + s[:1]
    
    return answer