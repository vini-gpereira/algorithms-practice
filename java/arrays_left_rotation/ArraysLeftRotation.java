import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class ArraysLeftRotation {

    // Complete the rotLeft function below.
    static int[] rotLeft(int[] a, int d) {
        int n = a.length;
        int[] rot = new int[n];

        for (int i = 0; i < n; i++) {
            rot[mod(i - d, n)] = a[i];
        }

        return rot;
    }

    private static int mod(int n, int m) {
        return (((n % m) + m) % m);
    }

    private static void printArray(int[] a) {
        for (int i = 0; i < a.length; i++) {
            System.out.print(a[i] + " ");
        }

        System.out.print("\n");
    }

    public static void main(String[] args) {
        int[] a = { 1, 2, 3, 4, 5 };
        int d = 4;
        int[] res = rotLeft(a, d);
        printArray(res);
    }
}
