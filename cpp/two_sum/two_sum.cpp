#include <iostream>
#include<vector>
#include<unordered_map>
using namespace std;


class Solution {
  public:
      vector<int> twoSum(vector<int>& nums, int target) {
          const int numsLen = nums.size();
          unordered_map<int, int> hash;
          vector<int> res;

          for (int i = 0; i < numsLen; i++) {
            int portion = target - nums[i];

            if (hash.count(portion)) {
              res.push_back(hash[portion]);
              res.push_back(i);
              return res;
            } else {
              hash[nums[i]] = i;
            }
          }

          return res;
      }
};


int main() {
  Solution sol;
  vector<int> nums = { 3,2,4 };
  vector<int>& numsRef = nums;
  int target = 6;

  vector<int> res = sol.twoSum(numsRef, target);

  if (res.size() == 2) {
    cout << "[" << res[0] << ", " << res[1] << "]" << endl;
  }

  return 0;
}
