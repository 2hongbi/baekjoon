import java.util.Scanner;

public class Main {

    public static boolean isPrime(int x) {
        if (x < 2) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(x); i++) {
            if (x % i == 0) {
                return false;
            }
        }

        return true;
    }

    public static boolean isPalindrome(int x) {
        String str = Integer.toString(x);
        int len = str.length();

        for (int  i = 0; i < len / 2; i++) {
            if (str.charAt(i) != str.charAt(len - i - 1)) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        while (true) {
            if (isPalindrome(n) && isPrime(n)) {
                System.out.println(n);
                break;
            }
            n++;
        }
        sc.close();
    }
}
