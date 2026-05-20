class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> numToIndex = {};

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (numToIndex.find(diff) != numToIndex.end()) {
                return {numToIndex[diff], i};
            }
            numToIndex[nums[i]] = i;
        }
        return {};
    }
};
