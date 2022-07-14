package level1.Q10871;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        st.nextToken();
        int X = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        while (st.hasMoreTokens()) {
            int val = Integer.parseInt(st.nextToken());
            if (val < X) {
                System.out.print(val + " ");
            }
        }
    }
}
