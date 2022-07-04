package level1.Q2562;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int max = -1;
        int index = 0;
        for (int i = 0; i < 9; i++) {
            int num = sc.nextInt();
            if (num > max) {
                max = num;
                index = i+1;
            }
        }
        sc.close();
        System.out.println(max);
        System.out.println(index);
    }
}
