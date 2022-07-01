package level1.Q1008;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println((double) a / b); // double - 11bit, 소수부분 15자리까지 오차없이 표현, float - 8bit, 소수부분 6자리까지 오차 없이 표현
    }
}
