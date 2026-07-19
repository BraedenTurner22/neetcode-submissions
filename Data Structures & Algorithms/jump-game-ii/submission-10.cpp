class Solution {
public:
    int jump(vector<int>& nums) {
        int result = 0;
        int l = 0, r = 0;

        while (r < nums.size()-1) {
            int maxJump = 0;
            for (int j = l; j <= r; j++) {
                maxJump = std::max(maxJump, j+nums[j]);
            }
            l = r+1;
            r = maxJump;
            result++;
        }

        return result;
    }
};
