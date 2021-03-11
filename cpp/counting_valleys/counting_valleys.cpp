#include <bits/stdc++.h>

using namespace std;

int countingValleys(int steps, string path) {
  int valleys = 0;
  int level = 0;
  int lastLevel = 0;
  for (int i = 0; i < path.size(); i++) {
    char step = path[i];
    lastLevel = level;
    if(step == 'D') {
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

int main() {
  const int steps = 8;
  string path = "UDDDUDUU";
  const int valleys = countingValleys(steps, path);
  cout << valleys << '\n';
  return 0;
}