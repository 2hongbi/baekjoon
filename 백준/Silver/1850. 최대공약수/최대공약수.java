import java.util.Scanner;

public class Main {

    public static long gcd(long a, long b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();

        long result = gcd(a, b);

        // 최대 공약수만큼 '1' 출력하기
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result; i++) {
            sb.append("1");
        }
        System.out.println(sb.toString());

        sc.close();
    }
}
