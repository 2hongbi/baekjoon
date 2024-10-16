from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())  # 문서의 개수, 궁금한 문서의 위치
    priorities = list(map(int, input().split()))

    queue = deque([(i, priorities[i]) for i in range(n)])
    print_order = 0 # 출력 우선순위

    while queue:
        current = queue.popleft()

        if any(current[1] < doc[1] for doc in queue):
            queue.append(current)
        else:
            print_order += 1
            if current[0] == m:
                print(print_order)
                break