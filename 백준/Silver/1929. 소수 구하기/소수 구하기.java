import java.util.*;


public class Main {

    public static boolean[] sieve_of_eratosthenes(int n) {
        boolean[] sieve = new boolean[n + 1];

        // 0과 1은 소수가 아님
        sieve[0] = false;
        sieve[1] = false;

        for (int i = 2; i <= n; i++) {
            sieve[i] = true;
        }

        for (int i = 2; i * i <= n; i++) {
            if (sieve[i]) {
                for (int j = i * i; j <= n; j += i) {
                    sieve[j] = false;
                }
            }
        }
        return sieve;
    }

    public static void printPrimesInRange(int m, int n) {
        boolean[] sieve = sieve_of_eratosthenes(n);

        for (int i = m; i <= n; i++) {
            if (sieve[i]) {
                System.out.println(i);
            }
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int m = sc.nextInt();
        int n = sc.nextInt();

        printPrimesInRange(m, n);

        sc.close();
    }
}
