import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class TwoDimensionalArrays {

    // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr) {
        int n = 6;
        int max = -63;
        int sum = max;

        for (int row = 1; row < n - 1; row++) {
            for (int col = 1; col < n - 1; col++) {
                sum = calculateHourglass(arr, row, col);
                if (sum > max) {
                    max = sum;
                }
            }
        }

        return max;
    }

    private static int calculateHourglass(int[][] arr, int row, int col) {
        int sum = arr[row - 1][col - 1] + arr[row - 1][col] + arr[row - 1][col + 1] + arr[row][col] + arr[row + 1][col - 1] + arr[row + 1][col] + arr[row + 1][col + 1];
        return sum;
    }

    public static void main(String[] args) {
        int[][] arr = {
            { 1, 1, 1, 0, 0, 0 },
            { 0, 1, 0, 0, 0, 0 },
            { 1, 1, 1, 0, 0, 0 },
            { 0, 0, 2, 4, 4, 0 },
            { 0, 0, 0, 2, 0, 0 },
            { 0, 0, 1, 2, 4, 0 }
        };

        int max = hourglassSum(arr);

        System.out.println("Max: " + max);
    }
}
