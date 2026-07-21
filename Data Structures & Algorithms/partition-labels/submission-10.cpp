class Solution {
public:
    vector<int> partitionLabels(string s) {

        std::unordered_map<char, int> lastIndex;
        std::vector<int> result;

        for (int i{0uz}; i < s.size(); ++i) {
            lastIndex[s[i]] = i;
        }

        int i = 0;
        while (i < s.size()) {
            int curr_max = lastIndex[s[i]];
            int counter = 0;
            for (int j = i; j <= curr_max; ++j) {
                curr_max = std::max(curr_max, lastIndex[s[j]]);
                counter++;
            }
            result.push_back(counter);
            i += counter;
        }
        return result;
    }
};
