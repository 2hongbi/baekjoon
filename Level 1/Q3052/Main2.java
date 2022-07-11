package level1.Q3052;

import java.util.ArrayList;
import java.util.Scanner;

public class Main2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> leftovers = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            int leftover = sc.nextInt() % 42;
            if (!leftovers.contains(leftover)) {
                leftovers.add(leftover);
            }
        }
        System.out.println(leftovers.size());
    }
}
