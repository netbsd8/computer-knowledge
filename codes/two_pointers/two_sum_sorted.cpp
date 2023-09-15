#include "../base.h"

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0;
        int right = numbers.size() - 1;

        while (left < right) {
            if (numbers[left] + numbers[right] == target) {
                vector<int> ret = {left + 1, right + 1};
                return ret;
            }

            if (numbers[left] + numbers[right] > target) {
                right -= 1;
            } else {
                left += 1;
            }
        }

        vector<int> ret = {};
        return ret;
    }
};