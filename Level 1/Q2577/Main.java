package level1.Q2577;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] quo = new int[10];
        int value = (sc.nextInt() * sc.nextInt() * sc.nextInt());

        while (value != 0) {
            quo[value % 10]++;
            value /= 10;
        }

        for (int q: quo) {
            System.out.println(q);
        }

        sc.close();
    }
}
