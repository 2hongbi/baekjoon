import java.util.Scanner;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Set;
import java.util.Collections;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine(); // 버퍼 비우기

        Set<String> log = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String[] input = sc.nextLine().split(" ");
            String name = input[0];
            String status = input[1];

            if (status.equals("enter")) {
                log.add(name);
            } else {
                log.remove(name);
            }
        }

        // Set -> ArrayList
        ArrayList<String> result = new ArrayList<>(log);
        Collections.sort(result, Collections.reverseOrder());

        for (String name : result) {
            System.out.println(name);
        }

        sc.close();
    }
}