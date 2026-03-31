class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        vector<vector<int>> response;

        for (auto m = 0; m < nums.size(); m++) {
            if (nums[m] > 0) {
                break;
            }
            if (m > 0 && nums[m] == nums[m-1]) {
                continue;
            }
            int l = m+1, r = nums.size()-1;
            while (l < r) {
                int sum = nums[m] + nums[l] + nums[r];
                if (sum > 0) {
                    r--;
                }
                else if (sum < 0) {
                    l++;
                }
                else {
                    response.push_back({nums[m], nums[l], nums[r]});
                    l++;
                    r--;
                    while (l<r && nums[l] == nums[l-1]) {
                        l++;
                    }
                }
            }
        }
        return response;
    }
};
