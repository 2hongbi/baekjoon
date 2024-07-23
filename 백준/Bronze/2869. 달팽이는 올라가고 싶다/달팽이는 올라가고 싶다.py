# https://www.acmicpc.net/problem/2869
# 높이 V미터, 낮에 A미터 올라가지만 밤에 B미터 미끄러짐
# 정상에 도달하면 미끄러지지 않음
# 1. 하루에 올라가는 실제 거리 : A - B
# 2. 정상에 도달하는 데 필요한 일 수 : 전체거리 V 중 마지막 날 낮에 올라가는 A 미터를 제외한 거리 (밤에만 미끄러짐)

import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

days = math.ceil((v - b) / (a - b))
print(days)