from collections import deque

n = int(input()) # 사람의 수

person1, person2 = map(int, input().split()) # 촌수 계산
m = int(input())

relations = [[] for _ in range(n + 1)]

# 그래프 구성
for _ in range(m):
    x, y = map(int, input().split())
    relations[x].append(y)
    relations[y].append(x)


def bfs(start, target):
    visited = [-1] * (n + 1)
    queue = deque([start])
    visited[start] = 0

    while queue:
        current = queue.popleft()
        for neighbor in relations[current]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                queue.append(neighbor)
                if neighbor == target:
                    return visited[neighbor]
    return -1


print(bfs(person1, person2))