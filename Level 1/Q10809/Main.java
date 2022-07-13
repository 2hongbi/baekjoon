package level1.Q10809;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        int[] alphabet = new int[26];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        Arrays.fill(alphabet, -1);

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (alphabet[ch - 97] == -1) {
                alphabet[ch - 97] = i;
            }
        }

        for (int a: alphabet) {
            System.out.print(a + " ");
        }

    }
}
