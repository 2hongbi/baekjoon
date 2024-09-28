from collections import deque

n, k = map(int, input().split())

visited = [0] * (max(k * 2 + 1, 100001))  

def bfs(n):
    queue = deque([n])

    while queue:
        curr_pos = queue.popleft()

        if curr_pos == k:
            return visited[curr_pos]

        for next_pos in (curr_pos - 1, curr_pos + 1, curr_pos * 2):
            if 0 <= next_pos < len(visited) and visited[next_pos] == 0:
                queue.append(next_pos)
                visited[next_pos] = visited[curr_pos] + 1

print(bfs(n))