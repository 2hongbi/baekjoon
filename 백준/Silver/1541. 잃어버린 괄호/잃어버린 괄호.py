expression = input().split('-')

answer = 0

for ex in expression[0].split('+'):
    answer += int(ex)

for i in range(1, len(expression)):
    for ex in expression[i].split('+'):
        answer -= int(ex)

print(answer)