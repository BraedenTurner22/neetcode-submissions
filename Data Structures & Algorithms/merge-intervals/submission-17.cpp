class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {

        std::sort(intervals.begin(), intervals.end());
        vector<vector<int>> results;
        results.push_back(intervals[0]);

        for (const auto& i : intervals) {
            if (results[results.size()-1][1] >= i[0]) {
                results[results.size()-1][1] = std::max(results[results.size()-1][1], i[1]);
            }
            else {
                results.push_back(i);
            }
        }

        return results;
    }
};
