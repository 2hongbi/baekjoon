import sys

input = sys.stdin.readline

n = int(input())
tree = {}

# 트리 정보 받기
for _ in range(n):
    node, left, right = input().strip().split()
    tree[node] = (left, right)
    

#전위: 루트 -> 왼 -> 오
def preorder(node):
    if node == '.':
        return
    print(node, end='') # 루트
    preorder(tree[node][0]) # 왼쪽
    preorder(tree[node][1]) # 오른쪽

# 중위: 왼 -> 루트 -> 오
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0]) # 왼쪽
    print(node, end='')
    inorder(tree[node][1]) # 오른쪽


# 후위: 왼 -> 오 -> 루트
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0]) # 왼쪽
    postorder(tree[node][1]) # 오른쪽
    print(node, end='') 


preorder('A')
print()
inorder('A')
print()
postorder('A')
print()