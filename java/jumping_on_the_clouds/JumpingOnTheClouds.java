import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class JumpingOnTheClouds {

    // Complete the jumpingOnClouds function below.
    static int jumpingOnClouds(int[] c) {
        int nextPos;
        int nClouds = c.length;
        int jumps = 0;
        int position = 0;

        while (position < nClouds - 1) {
            nextPos = position + 1;
            
            if (c[nextPos] == 0) {
                position = nextPos;
            }
            
            nextPos++;

            if (nextPos < nClouds && c[nextPos] == 0) {
                position = nextPos;
            }

            jumps++;
        }

        return jumps;
    }

    public static void main(String[] args) {
        int[] c = new int[]{ 0, 0, 0, 0, 1, 0 };
        int jumps = jumpingOnClouds(c);
        System.out.println(jumps);
    }
}
