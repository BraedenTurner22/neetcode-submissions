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
        
        std::vector<std::pair<int, int>> times;

        for (auto& i : intervals) {
            times.push_back({i.start, 1});
            times.push_back({i.end, -1});
        }

        std::sort(times.begin(), times.end(), [](auto& a, auto& b){
            return a.first == b.first ? a.second < b.second : a.first < b.first;
        });

        int res = 0, count = 0;
        for (auto& t : times) {
            count += t.second;
            res = std::max(res, count);
        }

        return res;
    }
};
