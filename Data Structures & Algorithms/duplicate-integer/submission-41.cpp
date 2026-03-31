class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> s1;

        for(int num : nums) {
            if (s1.contains(num)) {
                return true;
            }
            s1.insert(num);
        }
        return false;
    }
};