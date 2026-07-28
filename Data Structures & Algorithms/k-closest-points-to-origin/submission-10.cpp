class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        std::priority_queue<std::pair<int, std::pair<int, int>>> pq;
        std::vector<std::vector<int>> results;

        for (const auto& p : points) {
            int distance = p[0] * p[0] + p[1] * p[1];
            pq.push({distance, {p[0], p[1]}});
            if (pq.size() > k) {
                pq.pop();
            }
        }

        while (!pq.empty()) {
            auto coords = pq.top().second;
            results.push_back({coords.first, coords.second});
            pq.pop();
        }
        return results;
    }
};
