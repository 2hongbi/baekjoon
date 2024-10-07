import java.util.*;
public class Main {

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void bfs(int x, int y, int[][] farm, boolean[][] visited, int m, int n) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        visited[x][y] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int curr_x = current[0];
            int curr_y = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = curr_x + dx[i];
                int ny = curr_y + dy[i];

                if (nx >= 0 && nx < m && ny >= 0 && ny < n && farm[nx][ny] == 1 && !visited[nx][ny]) {
                    queue.add(new int[]{nx, ny});
                    visited[nx][ny] = true;
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int t = 0; t < T; t++) {
            int m = sc.nextInt();
            int n = sc.nextInt();
            int k = sc.nextInt();

            int[][] farm = new int[m][n];
            boolean[][] visited = new boolean[m][n];

            for (int i = 0; i < k; i++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                farm[x][y] = 1;
            }

            int wormCount = 0;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (farm[i][j] == 1 && !visited[i][j]) {
                        bfs(i, j, farm, visited, m, n);
                        wormCount++;
                    }
                }
            }
            System.out.println(wormCount);
        }
        sc.close();
    }
}
