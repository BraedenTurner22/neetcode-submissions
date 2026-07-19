class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {

        if (hand.size() % groupSize != 0) return false;

        std::unordered_map<int, int> count;

        for (const int& h : hand) count[h]++;

        for (int i{0uz}; i < hand.size(); ++i) {
            int start = i;
            while (count.contains(start-1)) start--;
            while (start <= hand[i]) {
                while (count[start] > 0) {
                    for (int j = start; j < start+groupSize; ++j) {
                        if (count[j] == 0) return false;
                        count[j]--;
                    }
                }
                start++;
            }
        }
        return true;
    }
};
