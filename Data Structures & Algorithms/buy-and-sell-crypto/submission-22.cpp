class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max = 0;

        int i = 0;
        while (i < prices.size()) {
            int j = i+1;
            while (j < prices.size() and prices[j] > prices[i]) {
                max = std::max(max, prices[j]-prices[i]);
                j++;
            }
            i = j;
        }
        return max;
    }
};
