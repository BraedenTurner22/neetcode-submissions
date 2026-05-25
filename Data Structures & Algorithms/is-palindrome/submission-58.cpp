class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = (int)s.size() - 1;
        while (l <= r) {
            while (!std::isalnum(s[l]) && l <= r) l++;
            while (!std::isalnum(s[r]) && l <= r) r--;
            if (std::tolower(s[l]) != std::tolower(s[r]) && l <= r) return false;

            l++;
            r--;
        }
        return true;
    }
};
