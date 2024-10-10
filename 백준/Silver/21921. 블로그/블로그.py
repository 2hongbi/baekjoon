n, x = map(int, input().split()) # 블로그를 시작하고 지난 일수, X일 동안
visitors = list(map(int, input().split()))

current_sum = sum(visitors[:x])
max_visitors = current_sum
count = 1

for i in range(x, n):
    current_sum += visitors[i] - visitors[i - x]

    if current_sum > max_visitors:
        max_visitors = current_sum
        count = 1
    elif current_sum == max_visitors:
        count += 1


print(max_visitors, count, sep='\n') if max_visitors else print("SAD")