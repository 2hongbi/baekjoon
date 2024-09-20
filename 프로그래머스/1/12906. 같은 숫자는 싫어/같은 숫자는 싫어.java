import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        List<Integer> result = new ArrayList<>();
        result.add(arr[0]);
        
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i-1]) {
                result.add(arr[i]);
            }
        }
            
        // 리스트를 배열로 변환해서 반환
        return result.stream().mapToInt(i -> i).toArray();
    }
}