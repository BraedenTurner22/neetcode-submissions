class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> dups = {};

        for (int& num : nums) {
            if (dups.contains(num)) return true;
            dups.insert(num);
        }

        return false;
    }
};