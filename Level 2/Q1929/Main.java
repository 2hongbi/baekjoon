package Level2.Q1929;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();
        int N = sc.nextInt();

        if (N <= 1)
            return;

        boolean[] primeList = new boolean[N + 1]; // false로 초기화됨
        primeList[0] = primeList[1] = true; // true = 소수 아님, false = 소수

        for (int i = 2; i <= Math.sqrt(primeList.length); i++) {
            if (primeList[i]) continue;
            for (int j = i * i; j < primeList.length; j += i) {
                primeList[j] = true;
            }
        }

        for (int i = M; i <= N; i++) {
            if (!primeList[i]) {  // false가 소수이므로 소수 출력
                System.out.println(i);
            }
        }
    }
}
