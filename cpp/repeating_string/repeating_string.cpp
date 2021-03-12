#include <bits/stdc++.h>

using namespace std;

// Complete the repeatedString function below.
long repeatedString(string s, long n) {
    long occurrences = 0;
    long subLen = s.size();
    long l = min(subLen, n);

    for (int i = 0; i < l; i++) {
        if (s[i] == 'a') {
            occurrences++;
        }
    }

    if (n > subLen) {
        occurrences = occurrences * (n / subLen);

        for (int j = 0; j < (n % subLen); j++) {
            if (s[j] == 'a') {
                occurrences++;
            }   
        }
    }

    return occurrences;
}

int main()
{
    string s = "ababa";
    long n = 3;
    long occurrences = repeatedString(s, n);
    cout << occurrences << '\n';
    return 0;
}
