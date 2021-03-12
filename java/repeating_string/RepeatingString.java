import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class RepeatingString {

    // Complete the repeatedString function below.
    static long repeatedString(String s, long n) {
        long strLen = s.length();
        long l = Math.min(strLen, n);
        long occur = 0;

        for (int j = 0; j < l; j++) {
            if (s.charAt(j) == 'a') {
                occur++;
            }
        }

        if (n > strLen) {
            occur = occur * (n / strLen);
        
            for (int i = 0; i < (n % strLen); i++) {
                if (s.charAt(i) == 'a') {
                    occur++;
                }
            }
        }


        return occur;
    }

    public static void main(String[] args) {
        String s = "ababa";
        long n = 3;
        long occur = repeatedString(s, n);
        System.out.println(occur);
    }
}
