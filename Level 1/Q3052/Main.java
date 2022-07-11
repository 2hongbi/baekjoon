package level1.Q3052;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Integer[] leftovers = new Integer[10];
        for (int i = 0; i < 10; i++) {
            leftovers[i] = (sc.nextInt() % 42);
        }
        sc.close();

        Set<Integer> result = new HashSet<Integer>(Arrays.asList(leftovers));
        System.out.println(result.size());
    }
}
