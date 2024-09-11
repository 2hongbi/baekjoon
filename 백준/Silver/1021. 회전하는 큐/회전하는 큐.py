from collections import deque

n, m = map(int, input().split())
queue = deque(range(1, n + 1))

target_list = list(map(int, input().split()))

count = 0
while len(target_list) > 0:
    target = target_list[0]
    target_index = queue.index(target)

    if target_index <= len(queue) // 2:
        # 왼쪽으로 회전
        queue.rotate(-target_index)
        count += target_index
    else:
        # 오른쪽 회전
        queue.rotate(len(queue) - target_index)
        count += len(queue) - target_index

    queue.popleft()
    target_list.pop(0)


print(count)