class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }
        std::unordered_map<char, int> sMap;
        std::unordered_map<char, int> tMap;

        for (int i=0; i < s.length(); i++) {
            sMap[s[i]]++;
            tMap[t[i]]++;
        }

        return sMap==tMap;
    }
};
