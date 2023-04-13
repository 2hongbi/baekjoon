def solution(number, k):
    collected = []
    for i, num in enumerate(number):
        # 빼낼 개수가 남아있고, 모아놓은 마지막 글자가 현재 꺼낸 것보다 작고, 모아놓은 글자가 0개보다 많을 때
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        
        if k == 0:
            collected += list(number[i:])
            break
        
        collected.append(num)
        
    collected = collected[:-k] if k > 0 else collected
    
    return ''.join(collected)