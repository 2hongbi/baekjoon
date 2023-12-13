class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        
        int index = 0;
        for (int num : numbers) {
            answer[index] = num * 2;
            index++;
        }
        
        return answer;
    }
}