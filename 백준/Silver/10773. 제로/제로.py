k = int(input())
stack = []

for _ in range(k):
    x = int(input())
    if x == 0:
        if stack:
            stack.pop()
        else:
            print(0)
    else:
        stack.append(x)


print(sum(stack))