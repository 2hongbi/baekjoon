package level1.Q10818;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Integer.parseInt(br.readLine()); // N 값인데 쓰이지 않으므로 받기만 하기
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        int min =  1000000;
        int max = -1000000;
        while (st.hasMoreTokens()) {
            int value = Integer.parseInt(st.nextToken());
            if (value < min) {
                min = value;
            }
            if (value > max) {
                max = value;
            }
        }

        System.out.println(min + " " + max);

    }
}
