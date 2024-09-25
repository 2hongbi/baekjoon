import math

min_val, max_val = map(int, input().split())

check = [True] * (max_val - min_val + 1) # True == 제곱 ㄴㄴ 수

for i in range(2, int(math.sqrt(max_val)) + 1):
    square = i * i

    # square의 배수가 min_val 이상 max_val 이하인 범위에서 제거하기
    start = (min_val + square - 1) // square * square # square의 배수 중 min_val 이상의 첫 값
    for j in range(start, max_val + 1, square):
        check[j - min_val] = False

result = sum(check)
print(result)