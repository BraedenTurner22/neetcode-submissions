class Solution {
public:
    vector<int> twoSum(vector<int>& s, int target) {
        int l = 0, r = s.size()-1;

        while (l <= r) {
            if (s[l] + s[r] > target && l <= r) {
                r--;
            }
            else if (s[l] + s[r] < target && l <= r) {
                l++;
            }
            else {
                return {l+1, r+1};
            }
        }
    }
};
