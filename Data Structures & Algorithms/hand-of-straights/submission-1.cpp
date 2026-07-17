class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {

        if (hand.size() % groupSize != 0) return false;

        std::unordered_map<int, int> count;
        for (const int& h : hand) count[h]++;

        for (const int& h : hand) {
            int start = h;
            while (count.contains(start-1)) start--;
            while (start <= h) {
                while (count[start] > 0) {
                    for (int i = start; i < start+groupSize; i++) {
                        if (count[i] == 0) return false;
                        count[i]--;
                    }
                }
                start++;
            }
        }

        return true;
    }
};
