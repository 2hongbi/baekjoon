class Solution {
    public String solution(int age) {
        String ta = String.valueOf(age);
        int diff = (int)Math.abs('a' - '0');
        
        String answer = "";
        for (int i=0;i<ta.length();i++) {
            answer += (char)(ta.charAt(i) + diff);
        }
        
        
        return answer;
    }
}