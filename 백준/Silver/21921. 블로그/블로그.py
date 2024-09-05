n, x = map(int, input().split()) # 블로그를 시작하고 지난 일수, X일 동안
visitors = list(map(int, input().split()))

# 첫 x일 동안의 방문자 수의 합을 초기값으로 설정: 슬라이딩 윈도우
current_sum = sum(visitors[:x])
max_visitors = current_sum
count = 1 # 기간

for i in range(x, n):
    current_sum += visitors[i] - visitors[i - x]

    if current_sum > max_visitors:
        max_visitors = current_sum
        count = 1
    elif current_sum == max_visitors:
        count += 1


if max_visitors == 0:
    print("SAD")
else:
    print(max_visitors)
    print(count)