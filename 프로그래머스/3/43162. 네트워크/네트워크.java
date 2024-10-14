import java.util.LinkedList;
import java.util.Queue;
    
class Solution {
    
    static void bfs(int[][] computers, int start, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

		int n = computers.length;

        while (!queue.isEmpty()) {
            int currNode = queue.poll();

            for (int neighbor = 0; neighbor < n; neighbor++) {
                if (computers[currNode][neighbor] == 1 && !visited[neighbor]) {
                    queue.add(neighbor);
                    visited[neighbor] = true;
                }
            }
        }
    }
    
    public int solution(int n, int[][] computers) {
        boolean[] visited = new boolean[n];
        
        int networkCount = 0;
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                bfs(computers, i, visited);
                networkCount++;
            }
        }
        
        return networkCount;
   }
}