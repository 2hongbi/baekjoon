package level1.Q1157;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] alphabet = new int[26];
        Scanner sc = new Scanner(System.in);
        String s = sc.next().toUpperCase();

        for (int i = 0; i < s.length(); i++) {
            alphabet[s.charAt(i) - 65]++;
        }

        int max = 0;
        char c = '?';
        for (int i = 0; i < alphabet.length; i++) {
            if (alphabet[i] > max) {
                max = alphabet[i];
                c = (char) (i + 65);
            } else if (alphabet[i] == max) {
                c = '?';
            }
        }
        System.out.println(c);
    }
}
