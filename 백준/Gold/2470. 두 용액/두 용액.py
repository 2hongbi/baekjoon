n = int(input())
waters = list(map(int, input().split()))

waters.sort()

close_0 = float('inf')
start, end = 0, n - 1
answer = []


while start < end:
    a, b = waters[start], waters[end]
    current_sum = a + b

    if abs(current_sum) < close_0:
        close_0 = abs(current_sum)
        answer = [str(a), str(b)]

    # 합이 양수인 경우, 더 작은 값을 만들기 위해서 end를 왼쪽으로 이동하기
    if current_sum > 0:
        end -= 1
    else: # 합이 음수인 경우, 더 큰 값을 만들기 위해 start를 오른쪽으로 이동하기
        start += 1

print(' '.join(answer))