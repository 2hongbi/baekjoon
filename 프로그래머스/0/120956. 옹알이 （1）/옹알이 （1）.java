class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        String[] babb = {"aya", "ye", "woo", "ma"};
        String tmp = "";
        
        for (String b : babbling) {
            for (String bab : babb) {
                tmp = b.replace(bab, " ");
                b = tmp;
            }
            
            if (b.isBlank()) {
                answer++;
            }   
        }
        return answer;
    }
}