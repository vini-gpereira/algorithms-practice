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

public class FrequencyQueries {

    // Complete the freqQuery function below.
    static List<Integer> freqQuery(List<List<Integer>> queries) {
        HashMap<Integer, Set<Integer>> freqsToEls = new HashMap<Integer, Set<Integer>>();
        HashMap<Integer, Integer> elsToFreqs = new HashMap<Integer, Integer>();
        List<Integer> result = new ArrayList<Integer>();

        int operationID, element;

        for (List<Integer> query : queries) {
            operationID = query.get(0);
            element = query.get(1);

            if (operationID == 1) {
                add(element, elsToFreqs, freqsToEls);
            } else if (operationID == 2) {
                remove(element, elsToFreqs, freqsToEls);
            } else {
                result.add(isSomeFrequencyEqualsTo(element, elsToFreqs, freqsToEls));
            }
        }

        return result;
    }

    private static void add(int element, HashMap<Integer, Integer> elsToFreqs, HashMap<Integer, Set<Integer>> freqsToEls) {
        Integer oldFrequency = elsToFreqs.getOrDefault(element, 0);
        Integer newFrequency = oldFrequency + 1;
        elsToFreqs.put(element, newFrequency);

        if (freqsToEls.containsKey(oldFrequency)) {
            freqsToEls.get(oldFrequency).remove(element);
        }

        freqsToEls.putIfAbsent(newFrequency, new HashSet<>());
        freqsToEls.get(newFrequency).add(element);
    }

    private static void remove(int element, HashMap<Integer, Integer> elsToFreqs, HashMap<Integer, Set<Integer>> freqsToEls) {
        Integer oldFrequency = elsToFreqs.getOrDefault(element, 0);
        Integer newFrequency = oldFrequency > 0 ? oldFrequency - 1 : 0;
        elsToFreqs.put(element, newFrequency);

        if (freqsToEls.containsKey(oldFrequency)) {
            freqsToEls.get(oldFrequency).remove(element);
        }

        freqsToEls.putIfAbsent(newFrequency, new HashSet<>());
        freqsToEls.get(newFrequency).add(element);
    }

    private static int isSomeFrequencyEqualsTo(int element, HashMap<Integer, Integer> elsToFreqs, HashMap<Integer, Set<Integer>> freqsToEls) {
        if (element == 0 || freqsToEls.getOrDefault(element, Collections.emptySet()).size() > 0) {
            return 1;
        }

        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int q = Integer.parseInt(bufferedReader.readLine().trim());

        List<List<Integer>> queries = new ArrayList<>();

        IntStream.range(0, q).forEach(i -> {
            try {
                queries.add(
                    Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
                        .map(Integer::parseInt)
                        .collect(toList())
                );
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        List<Integer> ans = freqQuery(queries);

        System.out.println(ans);
    }
}
