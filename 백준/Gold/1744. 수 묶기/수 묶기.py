from queue import PriorityQueue

n = int(input())

plus_pq = PriorityQueue()
minus_pq = PriorityQueue()
one_cnt = 0
zero_cnt = 0

for _ in range(n):
    num = int(input())

    # 양수 내림차순 정렬을 위해 -1을 곱하여 저장
    if num > 1:
        plus_pq.put(num * -1)
    elif num < 0:
        minus_pq.put(num)
    elif num == 1:
        one_cnt += 1
    elif num == 0:
        zero_cnt += 1


result = 0

while plus_pq.qsize() > 1:
    data1 = plus_pq.get() * -1
    data2 = plus_pq.get() * -1
    result += data1 * data2

if plus_pq.qsize() > 0:
    result += plus_pq.get() * -1

while minus_pq.qsize() > 1:
    data1 = minus_pq.get()
    data2 = minus_pq.get()
    result += data1 * data2

if minus_pq.qsize() > 0:
    if zero_cnt == 0:
        result += minus_pq.get()

result += one_cnt

print(result)