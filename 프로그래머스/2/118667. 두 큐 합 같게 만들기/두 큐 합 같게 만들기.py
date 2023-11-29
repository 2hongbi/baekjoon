from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)   # 입력받은 리스트 queue로 변환 : O(1)
    sum1, sum2 = sum(queue1), sum(queue2)
    total_sum = sum1 + sum2
    
    # 두 큐의 총합이 홀수라면, 같게 만들 수 없음
    if total_sum % 2 != 0:
        return -1
    
    target_sum = total_sum // 2
    max_iterations = len(queue1) + len(queue2) * 2 # 최대 반복 횟수 설정하기
    
    idx1, idx2 = 0, 0
    
    while answer < max_iterations:
        if sum1 > target_sum:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
        elif sum1 < target_sum:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
        else:
            return answer
        answer += 1
    
    return -1