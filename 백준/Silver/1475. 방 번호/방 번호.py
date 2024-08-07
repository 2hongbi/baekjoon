# https://www.acmicpc.net/problem/1475
# 다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다.
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오.
# (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)
from collections import Counter

def min_sets_needed(room_number):
    counter = Counter(room_number)

    count_6_and_9 = counter['6'] + counter['9']

    # 필요 세트 수
    counter['6'] = counter['9'] = (count_6_and_9 + 1) // 2

    return max(counter.values())


num = input()
print(min_sets_needed(num))