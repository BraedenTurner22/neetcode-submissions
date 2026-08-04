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

        std::vector<std::pair<int, int>> allTimes;

        for (auto& i : intervals) {
            int s = i.start;
            int e = i.end;
            allTimes.push_back({s, 1});
            allTimes.push_back({e, -1});
        }

        std::sort(allTimes.begin(), allTimes.end(), [](auto& a, auto& b){
            return a.first == b.first ? a.second < b.second : a.first < b.first;
        });

        int result = 0, count = 0;
        for (auto& t : allTimes) {
            count += t.second;
            result = std::max(result, count);
        }

        return result;
    }
};
