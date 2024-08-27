# A: 고정비용, B: 한 대의 노트북을 생산하는 데 드는 비용, C: 노트북 가격
a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print(a // (c - b) + 1)