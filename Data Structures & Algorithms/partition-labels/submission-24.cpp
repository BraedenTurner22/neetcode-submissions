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
            int counter = 0;
            for (int j = i; j <= stoppingPoint; ++j) {
                stoppingPoint = std::max(stoppingPoint, lastIndex[s[j]]);
                counter++;
            }
            results.push_back(counter);
            i += counter;
        }
        return results;
    }
};
