import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();

        int k = sc.nextInt();

        for (int i = 0; i < k; i++) {
            int x = sc.nextInt();

            if (x == 0) {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else {
                    System.out.println(0);
                }
            } else {
                stack.push(x);
            }
        }

        int sum = 0;
        for (int value : stack) {
            sum += value;
        }
        System.out.println(sum);
        sc.close();

    }
}
