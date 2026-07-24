class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        
        std::vector<std::vector<int>> result;

        for (int i{0}; i < intervals.size(); ++i) {
            int& start = newInterval[0];
            int& end = newInterval[1];
            if (intervals[i][0] > end) {
                result.push_back(newInterval);
                copy(intervals.begin()+i, intervals.end(), back_inserter(result));
                return result;
            }
            else if (intervals[i][1] < start) {
                result.push_back(intervals[i]);
            }
            else {
                start = std::min(start, intervals[i][0]);
                end = std::max(end, intervals[i][1]);
            }
        }
        result.push_back(newInterval);
        return result;
    }
};
