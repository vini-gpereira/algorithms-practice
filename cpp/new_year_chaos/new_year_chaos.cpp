#include <bits/stdc++.h>

using namespace std;

void bribe(vector<int> q, int i, int j);
void printArray(vector<int>, int);

// Complete the minimumBribes function below.
void minimumBribes(vector<int> q) {
    int n = q.size();
    int bribes = 0;
    int person, i, j;

    for (i = 0; i < n; i++) {
        person = q[i];

        if (person - 1 - i > 2) {
            cout << "Too chaotic" << endl;
            return;
        }

        for (j = person - 2; j < i; j++) {
            if (q[j] > person) {
                bribes++;
            }
        }
    }

    cout << bribes << endl;
}

void bribe(vector<int> q, int i, int j) {  
    int temp = q[i];  
    q[i] = q[j];  
    q[j] = temp;  
}

void printArray(vector<int> arr, int size) {  
    int i;  
    for (i = 0; i < size; i++)  
        cout << arr[i] << " ";  
    cout << endl;  
}  

int main()
{
    vector<int> q = {2, 5, 1, 3, 4};
    minimumBribes(q);
    return 0;
}
