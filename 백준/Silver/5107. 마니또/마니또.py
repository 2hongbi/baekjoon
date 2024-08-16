# https://www.acmicpc.net/problem/5107
# union-find(disjoint set; 서로소 집합)는 그래프에서 연결 요소를 찾거나, 사이클을 검출하는 데 자주 사용됨
# 예를 들어 크루스칼 알고리즘을 사용해 최소 신장 트리를 찾을 때 핵심적인 역할을 함
import sys
input = sys.stdin.readline

def find(x):
    # 특정 원소가 속한 집합의 대표자 찾기
    if x != parent[x]:
        parent[x] = find(parent[x])
    return x

def union(x, y):
    # 두 집합을 하나로 합치기
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


tc_cnt = 0
while True:
    n = int(input())

    if n == 0:
        break

    parent = [i for i in range(n + 1)]
    tc_cnt += 1
    m = {}

    for _ in range(n):
        node1, node2 = map(str, input().split())

        if not node1 in m:
            m[node1] = len(m) + 1
        if not node2 in m:
            m[node2] = len(m) + 1

        union(parent[m[node1]], parent[m[node2]])

    parent = set(parent)
    print(tc_cnt, len(parent) - 1)