from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    pq.put(int(input()))

data1, data2 = 0, 0
sum = 0

while pq.qsize() > 1:
    data1, data2 = pq.get(), pq.get()
    temp = data1 + data2
    sum += temp
    pq.put(temp)

print(sum)