class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded;
        for (const string& str : strs) {
            encoded += to_string(str.size()) + "#" + str;
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> strings;

        int i = 0;
        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') j++;
            int num = stoi(s.substr(i, j-i));
            strings.push_back(s.substr(j+1, num));
            i = j + 1 + num;
        }

        return strings;
    }
};
