package level1.Q11720;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        br.readLine();

        int sum = 0;

        for (byte b: br.readLine().getBytes()) {
            sum += (b - '0');
        }

        System.out.println(sum);
    }
}
