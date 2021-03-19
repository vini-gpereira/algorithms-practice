import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

class MutableInt {
    private int value = 1;
    
    public MutableInt increment () { 
        ++value;
        return this;
    }

    public MutableInt decrement() {
        --value;
        return this;
    }

    public int get () {
        return value;
    }
}

public class RansomNote {

    // Complete the checkMagazine function below.
    static void checkMagazine(String[] magazine, String[] note) {
        HashMap<String, MutableInt> freq = new HashMap<String, MutableInt>();
        int m = magazine.length;
        int n = note.length;
        MutableInt count;
        String word;
        int i, j;

        for (i = 0; i < m; i++) {
            word = magazine[i];
            count = freq.get(word);
            if (count == null) {
                freq.put(word, new MutableInt());
            } else {
                count.increment();
            }
        }

        for (j = 0; j < n; j++) {
            word = note[j];
            count = freq.get(word);
            if (count == null || count.decrement().get() < 0) {
                System.out.println("No");
                return;
            }
        }

        System.out.println("Yes");
    }

    private static void printFreq(HashMap<String, MutableInt> freq) {
        MutableInt value;
        for (String key : freq.keySet()) {
            value = freq.get(key);
            System.out.println(key + ": " + value.get());
        }
    }

    public static void main(String[] args) {
        String[] magazine = { "give", "me", "one", "grand", "today", "night" };
        String[] note = { "give", "one", "grand", "today" };
        checkMagazine(magazine, note);
    }
}
