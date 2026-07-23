class Solution {
public:
    vector<int> partitionLabels(string s) {

        std::vector<int> results;
        std::unordered_map<char, int> lastIndex;

        for (int i{0}; i < s.size(); ++i) {
            lastIndex[s[i]] = i;
        }

        int i = 0;
        while (i < s.size()) {
            int stoppingPoint = lastIndex[s[i]];
            for (int j = i; j <= stoppingPoint; ++j) {
                stoppingPoint = std::max(stoppingPoint, lastIndex[s[j]]);
            }
            results.push_back(stoppingPoint-i+1);
            i = stoppingPoint+1;
        }
        return results;
    }
};