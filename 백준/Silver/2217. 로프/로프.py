n = int(input())
ropes = [int(input()) for _ in range(n)]

ropes.sort()
# k개의 로프 중 가장 약한 로프가 버틸 수 있는 중량에 k의 값
# k개의 로프를 사용해서 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸림
# 즉, 로프 * 연결하는 로프의 수로 최대 중량 구할 수 있음

max_weight = 0
for i in range(n):
    weight = ropes[i] * (n - i)
    max_weight = max(max_weight, weight)

print(max_weight)
