from functools import reduce

arr = []
for i in range(3):
    arr.append(int(input()))
mul = str(reduce(lambda x, y: x * y, arr))

for i in range(10):
    print(mul.count(str(i)))