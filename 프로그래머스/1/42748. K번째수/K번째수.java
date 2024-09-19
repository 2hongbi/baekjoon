import java.util.Arrays;

class Solution {
    
    public int getIndex(int[] array, int[] commands) {
        int i = commands[0] - 1;
        int j = commands[1];
        int target = commands[2];

        int[] newArray = Arrays.copyOfRange(array, i, j);
        Arrays.sort(newArray);

        // System.out.println(Arrays.toString(newArray));
        
        int result = newArray[target - 1];
        

        return result;
    }   
    
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for (int x = 0; x < commands.length; x++) {
            answer[x] = getIndex(array, commands[x]);
        }
        
        
        return answer;
    }
}