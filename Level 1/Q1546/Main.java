package level1.Q1546;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();
        int[] scores = new int[num];

        int max = -1;
        for (int i = 0; i < scores.length; i++) {
            int score = sc.nextInt();
            scores[i] = score;
            if (score > max) {
                max = score;
            }
        }

        double sum = 0;
        for (int i = 0; i < scores.length; i++) {
            int score = scores[i];
            sum += (((float) score / max) * 100);

        }
        System.out.println(sum / num);
    }
}
