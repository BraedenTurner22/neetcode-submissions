class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

        if (std::accumulate(gas.begin(), gas.end(), 0) < std::accumulate(cost.begin(), cost.end(), 0)) return -1;

        int start = 0;
        int total = 0;
        for (int i{0uz}; i < gas.size(); ++i) {
            total += (gas[i] - cost[i]);

            if (total < 0) {
                total = 0;
                start = i + 1;
            }
        }

        return start;
    }
};
