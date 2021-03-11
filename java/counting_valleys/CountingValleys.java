import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

public class CountingValleys {
    public static int countingValleys(int steps, String path) {
    // Write your code here
        int valleys = 0;
        int level = 0;
        int lastLevel = 0;
        char step;
        Map<Integer, Integer> socks = new HashMap<>();
        for (int i = 0; i < path.length(); i++) {
            step = path.charAt(i);
            lastLevel = level;
            if (step == 'D') {
                level--;
            } else {
                level++;
            }
            if (lastLevel < 0 && level == 0) {
                valleys++;
            }
        }
        return valleys;
    }

    public static void main(String[] args) {
        int steps = 8;
        String path = new String("UDDDUDUU");
        int result = countingValleys(steps, path);
        System.out.println(result);
    }
}