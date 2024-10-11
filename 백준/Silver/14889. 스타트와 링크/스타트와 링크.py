import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

min_diff = float('inf')
team = [False] * n  # False는 링크 팀, True는 스타트팀

def calculate_team_score():
    start_score, link_score = 0, 0
    for i in range(n):
        for j in range(n):
            if team[i] and team[j]:
                start_score += s[i][j]
            elif not team[i] and not team[j]:
                link_score += s[i][j]
    return abs(start_score - link_score)

def backtrack(depth, idx):
    global min_diff

    if depth == n // 2:
        min_diff = min(min_diff, calculate_team_score())
        return

    for i in range(idx, n):
        if not team[i]:
            team[i] = True # 스타트 팀 배정
            backtrack(depth + 1, i + 1)
            team[i] = False


backtrack(0, 0)
print(min_diff)