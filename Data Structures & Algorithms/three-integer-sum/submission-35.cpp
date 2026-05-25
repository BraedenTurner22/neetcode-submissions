class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> results;
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            if (nums[i] > 0) break;

            int l = i+1, r = nums.size()-1;
            while (l < r) {
                if (nums[i] + nums[l] + nums[r] < 0) l++;
                else if (nums[i] + nums[l] + nums[r] > 0) r--;
                else {
                    results.push_back({nums[i], nums[l], nums[r]});
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l-1]) l++;
                    }
            }
        }
        return results;
    }
};
