n = int(input())
a = list(map(int, input().split()))

stack = []
result = [-1] * n # 결과 저장 리스트, 초기값 -1 설정

for i in range(n):
    # 현재 원소가 스택의 top에 해당하는 원소보다 크면 오큰수 찾음
    while stack and a[stack[-1]] < a[i]:
        index = stack.pop()
        result[index] = a[i]

    # 현재 원소의 인덱스를 스택에 저장
    stack.append(i)

print(' '.join(map(str, result)))