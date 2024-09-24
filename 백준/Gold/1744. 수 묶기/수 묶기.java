import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        List<Integer> positive = new ArrayList<>();
        List<Integer> negative = new ArrayList<>();

        int zeros = 0, ones = 0, result = 0;

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();

            if (num > 1) {
                positive.add(num);
            } else if (num == 0) {
                zeros++;
            } else if (num == 1) {
                ones++;
            } else {
                negative.add(num);
            }
        }

        // 양수는 내림차순
        Collections.sort(positive, Collections.reverseOrder());
        // 음수는 오름차순
        Collections.sort(negative);

        // 양수 두 개씩 묶어 곱하기
        for (int i = 0; i < positive.size() - 1; i += 2) {
            result += positive.get(i) * positive.get(i + 1);
        }

        if (positive.size() % 2 == 1) {
            result += positive.get(positive.size() - 1);
        }

        // 음수 두 개씩 묶어 곱하기
        for (int i = 0; i < negative.size() - 1; i += 2) {
            result += negative.get(i) * negative.get(i + 1);
        }

        if (negative.size() % 2 == 1 && zeros == 0) {
            result += negative.get(negative.size() - 1);
        }

        result += ones;

        System.out.println(result);
        sc.close();
    }
}