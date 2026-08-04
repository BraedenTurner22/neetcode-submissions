/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](auto& a, auto& b){
            return a.start < b.start;
        });


        for (int i{1}; i < intervals.size(); ++i) {
            Interval prevInterval = intervals[i-1];
            Interval currInterval = intervals[i];
            if (prevInterval.end > currInterval.start) return false;
        }

        return true;
    }
};
