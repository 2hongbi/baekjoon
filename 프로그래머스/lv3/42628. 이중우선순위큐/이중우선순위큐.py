import heapq


def solution(operations):
    heap = []
    for op in operations:
        operation, num = op.split()
        if operation == 'I':
            heapq.heappush(heap, int(num))
        else:
            if not heap:
                continue
            if num == '-1':
                heapq.heappop(heap)  # 가장 작은 원소를 힙에서 제거
            else:
                print(heapq.nlargest(1, heap))
                heap.remove(heapq.nlargest(1, heap)[0])  # n개의 큰 원소 찾기
    return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]] if heap else [0, 0] 