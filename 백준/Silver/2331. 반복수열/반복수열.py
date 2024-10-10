a, p = map(int, input().split())

visited = []
visited.append(a)

def next_number(num, p):
    total = 0
    while num > 0:
        total += (num % 10) ** p
        num //= 10
    return total

answer = 0
while True:
    next_num = next_number(visited[-1], p) # 수열의 다음 숫자 생성

    if next_num in visited: # 이미 방문한 숫자가 나오면 방문이 시작됨
        answer = visited.index(next_num)
        break

    visited.append(next_num)

print(answer)