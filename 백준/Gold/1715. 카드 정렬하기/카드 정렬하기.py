from queue import PriorityQueue

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    date = int(input())
    pq.put(date)

data1 = 0
data2 = 0
sum = 0

while pq.qsize() > 1:
    data1 = pq.get()
    data2 = pq.get()
    temp = data1 + data2
    sum += temp
    pq.put(temp)

print(sum)