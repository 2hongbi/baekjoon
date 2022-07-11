package level1.Q8958;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] answers = new String[sc.nextInt()];

        for (int i = 0; i < answers.length; i++) {
            answers[i] = sc.next();
        }

        for (int i = 0; i < answers.length; i++) {
            int sum = 0;
            int count = 0;
            for (int j = 0; j < answers[i].length(); j++) {
                if (answers[i].charAt(j) == 'O') {
                    count += 1;
                    sum += count;
                } else {
                    count = 0;
                }
            }
            System.out.println(sum);
        }
    }
}
