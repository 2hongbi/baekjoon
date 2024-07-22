# https://www.acmicpc.net/problem/14562
# <연속 발차기의 두 가지 방법>
# A는 현재 점수만큼 점수를 얻을 수 있는 엄청난 연속 발차기이다. 하지만 상대 역시 3점을 득점하는 위험이 있다.
# B는 1점을 얻는 연속 발차기이다.

from collections import deque

def bfs(s, t):
    queue = deque([(s, t, 0)])  # 현재 점수, 상대 점수, 연속 발차기 점수

    while queue:
        current_score, opponent_score, kicks = queue.popleft()

        if current_score == opponent_score:
            return kicks

        if current_score < opponent_score:
            queue.append((current_score * 2, opponent_score + 3, kicks + 1))
            queue.append((current_score + 1, opponent_score, kicks + 1))

    return -1



tc = int(input())
for _ in range(tc):
    s, t = map(int, input().split())
    print(bfs(s, t))