class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set seenValues(nums.begin(), nums.end());
        int longest = 0;

        for (int& num : nums) {
            if (seenValues.contains(num-1)) continue;

            int i = 0;
            int curr = num;
            while (seenValues.contains(curr)) {
                i++;
                curr++;
            }
            longest = std::max(longest, i);
        }
        return longest;
    }
};
