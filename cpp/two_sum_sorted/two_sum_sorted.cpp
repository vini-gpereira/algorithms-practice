#include <iostream>
#include<vector>
#include<unordered_map>
using namespace std;


class Solution {
    private:
        int binarySearch(vector<int>& numbers, int val, int first, int end) {
            int medium = (end + first) / 2;

            if (first > end) {
                return -1;
            }

            if (numbers[medium] == val) {
                return medium;
            }

            if (val < numbers[medium]) {
                return binarySearch(numbers, val, first, medium - 1);
            }

            return binarySearch(numbers, val, medium + 1, end);
        }

    public:
        vector<int> bsSolution(vector<int>& numbers, int target) {
            const int len = numbers.size();

            for (int i = 0; i < len - 1; i++) {
                int diff = target - numbers[i];
                int diffIdx = binarySearch(numbers, diff, i, len - 1);

                if (diffIdx != -1) {
                    return vector<int> { i, diffIdx };
                }
            }

            return vector<int> { -1, -1 };
        }

        vector<int> optimizedBsSolution(vector<int>& numbers, int target) {
            int i, diff, diffIdx;
            const int len = numbers.size();

            while (i < len - 1 && numbers[i] < target) {
                diff = target - numbers[i];
                diffIdx = binarySearch(numbers, diff, i, len - 1);

                if (diffIdx != -1) {
                    return vector<int> { i, diffIdx };
                }

                i++;
            }

            return vector<int> { -1, -1 };
        }

        vector<int> hashSolution(vector<int>& numbers, int target) {
            const int len = numbers.size();
            unordered_map<int, int> map;

            for (int i = 0; i < len; i++) {
                int complement = target - numbers[i];

                if (map.count(complement)) {
                return vector<int> { map[complement], i };
                } else {
                map[numbers[i]] = i;
                }
            }

            return vector<int> { -1, -1 };
        }
     
        vector<int> twoPointersSolution(vector<int>& numbers, int target) {
            int left = 0, right = numbers.size() - 1;
            
            while (left < right) {
                int sum = numbers[left] + numbers[right];
                if (sum > target)
                    right--;
                else if (sum < target)
                    left++;
                else
                    return { left, right };
            }
            return {}; 
        }
};


int main() {
    Solution sol;
    int target;
    vector<int> nums, res;
    
    nums = { 2, 7, 11, 15 };
    target = 9;
    
    vector<int>& numsRef = nums;

    res = sol.bsSolution(numsRef, target);

    if (res.size() == 2) {
        cout << "Binary Search solution: ";
        cout << "[" << res[0] << ", " << res[1] << "]" << endl;
    }

    res = sol.optimizedBsSolution(numsRef, target);

    if (res.size() == 2) {
        cout << "Optimized Binary Search solution: ";
        cout << "[" << res[0] << ", " << res[1] << "]" << endl;
    }

    res = sol.hashSolution(numsRef, target);

    if (res.size() == 2) {
        cout << "Hash solution: ";
        cout << "[" << res[0] << ", " << res[1] << "]" << endl;
    }

    res = sol.twoPointersSolution(numsRef, target);

    if (res.size() == 2) {
        cout << "Two Pointers solution: ";
        cout << "[" << res[0] << ", " << res[1] << "]" << endl;
    }

  return 0;
}
