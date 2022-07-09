package level1.Q2884;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int min = sc.nextInt();

        boolean big = false;

        if (45 > min) {
            min = (min + 60) - 45;
            big = true;
        } else {
            min -= 45;
        }

        if (big) {
            if (hour == 0) {
                hour = 23;
            } else {
                hour--;
            }
        }

        System.out.println(hour + " " + min);

        sc.close();
    }
}
