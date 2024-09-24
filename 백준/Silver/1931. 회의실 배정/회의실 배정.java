import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        List<int[]> meetings = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            meetings.add(new int[] {start, end});
        }

        // 종료 시각 기준으로 정렬하기
        meetings.sort((a, b) -> {
            if (a[1] == b[1]) {
                return Integer.compare(a[0], b[0]);
            } else {
                return Integer.compare(a[1], b[1]);
            }
        });

        // 회의 선택하기
        int count = 1;
        int end_time = meetings.get(0)[1];

        for (int i = 1; i < n; i++) {
            if (meetings.get(i)[0] >= end_time) {
                count++;
                end_time = meetings.get(i)[1];
            }
        }

        System.out.println(count);
        sc.close();
    }
}

