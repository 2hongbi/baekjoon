n = int(input())

bag5 = n // 5

while bag5 >= 0:
    remainder = n - bag5 * 5
    # 남은 무게를 3 봉지로 담을 수 있나
    if remainder % 3 == 0:
        bag3 = remainder // 3
        print(bag5 + bag3)
        break
    bag5 -= 1

else:
    print(-1)