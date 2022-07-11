num = int(input())
for _ in range(num):
    answer = list(input())
    score = 0
    count = 0
    for a in answer:
        if a == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)