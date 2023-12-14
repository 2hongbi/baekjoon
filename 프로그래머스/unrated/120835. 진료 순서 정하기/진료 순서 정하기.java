import java.util.*;

class Solution {
    public int[] solution(int[] emergency) {
        int len = emergency.length;
        int[] answer = new int[len];
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < len; i++) {
            map.put(emergency[i], i);
        }
        
        Arrays.sort(emergency);
        
        for (int i = len - 1;i >= 0;i--) {
            answer[map.get(emergency[i])] = len - i;
        }
        
        return answer;
    }
}