class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;

        std::map<char, int> sMap = {};
        std::map<char, int> tMap = {};

        for (int i = 0; i < s.size(); i++) {
            sMap[s[i]] += 1;
            tMap[t[i]] += 1;
        }

        return (sMap == tMap);
    }
};
