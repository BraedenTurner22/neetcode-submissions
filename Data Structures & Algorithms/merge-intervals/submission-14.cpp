class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {

        std::sort(intervals.begin(), intervals.end());
        vector<vector<int>> results;
        results.push_back(intervals[0]);

        for (int i = 1; i < intervals.size(); ++i) {
            if (intervals[i][0] <= results[results.size()-1][1]) {
                results[results.size()-1] = {results[results.size()-1][0], std::max(results[results.size()-1][1], intervals[i][1])};
            }
            else results.push_back(intervals[i]);
        }

        return results;
    }
};
