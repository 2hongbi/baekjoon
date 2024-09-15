from queue import PriorityQueue

n = int(input())

pq = PriorityQueue()
for _ in range(n):
    pq.put(int(input()))

data1, data2 = 0, 0
total = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2
    total += temp
    pq.put(temp)

print(total)