import sys
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
target = int(input())

def dfs(node):
    tree[node] = -10
    for i in range(n):
        if node == tree[i]:
            dfs(i)

dfs(target)

count = 0
for i in range(n):
    if tree[i] != -10 and i not in tree:
        count += 1

print(count)