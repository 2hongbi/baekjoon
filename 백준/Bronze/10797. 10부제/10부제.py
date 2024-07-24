# https://www.acmicpc.net/problem/10797
# 자동차 10부제는 자동차 번호의 일의 자리 숫자와 날짜의 일의 자리 숫자가 일치하면 해당 자동차의 운행을 금지하는 것
# 위반하는 자동차의 대수를 출력하기

day = int(input())
cars = list(map(int, input().split()))

answer = 0
for c in cars:
    if c % 10 == day:
        answer += 1

print(answer)