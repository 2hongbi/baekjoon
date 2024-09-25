import java.util.*;
public class Main {

    static int[] dxs = {-1, 0, 1, 0};
    static int[] dys = {0, 1, 0, -1};
    static int[][] paper;
    static int n, m;

    public static int bfs(int x, int y) {
        int area = 1;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        paper[x][y] = 0; // 방문 처리

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cx = current[0];
            int cy = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dxs[i];
                int ny = cy + dys[i];

                if (0 <= nx && nx < n && 0 <= ny && ny < m && paper[nx][ny] == 1) {
                    area++;
                    paper[nx][ny] = 0;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
        return area;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();

        paper = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                paper[i][j] = sc.nextInt();
            }
        }

        int count = 0;
        int maxArea = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (paper[i][j] == 1) {
                    count++;
                    maxArea = Math.max(maxArea, bfs(i, j));
                }
            }
        }

        System.out.println(count);
        System.out.println(maxArea);

        sc.close();
    }
}
