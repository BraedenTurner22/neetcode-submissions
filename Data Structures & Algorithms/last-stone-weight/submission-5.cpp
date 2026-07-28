class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::make_heap(stones.begin(), stones.end());

        while (stones.size() > 1) {
            int stone1 = stones.front();
            std::pop_heap(stones.begin(), stones.end());
            stones.pop_back();

            int stone2 = stones.front();
            std::pop_heap(stones.begin(), stones.end());
            stones.pop_back();

            if (std::abs(stone1-stone2) > 0) {
                stones.push_back(std::abs(stone1-stone2));
                std::push_heap(stones.begin(), stones.end());
            }
        }

        if (!stones.empty()) return stones.front();
        else return 0;
    }
};
