from collections import deque

def solution(n, computers):
    visited = [False] * n
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            curr_node = queue.popleft()
            
            for neighbor in range(n):
                if computers[curr_node][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
            
    
    network_count = 0
    for i in range(n):
        if not visited[i]:
            bfs(i)
            network_count += 1
    
    return network_count