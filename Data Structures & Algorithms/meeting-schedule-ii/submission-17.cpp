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
    int minMeetingRooms(vector<Interval>& intervals) {

        std::vector<int> starts;
        std::vector<int> ends;

        for (auto& i : intervals) {
            starts.push_back(i.start);
            ends.push_back(i.end);
        }

        std::sort(starts.begin(), starts.end());
        std::sort(ends.begin(), ends.end());

        int s = 0, e = 0;

        int res = 0, count = 0;
        while (s < intervals.size()) {
            if (starts[s] < ends[e]) {
                count++;
                s++;
            }
            else {
                count--;
                e++;
            }
            res = std::max(res, count);
        }

        return res;
    }
};
