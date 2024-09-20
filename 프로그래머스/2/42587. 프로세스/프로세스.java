import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        // 큐를 생성하고, 프로세스의 우선순위와 인덱스를 저장
        Queue<int[]> queue = new LinkedList<>();
        
        // 우선순위 배열과 인덱스를 큐에 저장
        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new int[] { i, priorities[i] }); // {인덱스, 우선순위}
        }
        
        // 실행된 프로세스 순서를 추적할 변수
        int executionOrder = 0;

        // 큐가 빌 때까지 반복
        while (!queue.isEmpty()) {
            // 큐에서 가장 앞의 프로세스를 꺼냄
            int[] currentProcess = queue.poll();
            boolean hasHigherPriority = false;
            
            // 현재 프로세스보다 높은 우선순위가 있는지 확인
            for (int[] process : queue) {
                if (process[1] > currentProcess[1]) {
                    hasHigherPriority = true;
                    break;
                }
            }
            
            if (hasHigherPriority) {
                // 우선순위가 더 높은 프로세스가 있으면 다시 큐에 넣음
                queue.offer(currentProcess);
            } else {
                // 실행된 프로세스 순서를 증가시킴
                executionOrder++;
                
                // 현재 프로세스가 목표 프로세스(location)인지 확인
                if (currentProcess[0] == location) {
                    return executionOrder;
                }
            }
        }
        
        return -1; // 예외 처리, 보통은 여기까지 오지 않음
    }
}