class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currMax = nums[0];
        int max = nums[0];

        for (int i{1uz}; i < nums.size(); ++i) {
            currMax = std::max(currMax + nums[i], nums[i]);
            max = std::max(currMax, max);
        }

        return max;
    }
};
