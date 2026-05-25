class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maxWater = 0;
        int l = 0, r = heights.size()-1;

        while (l < r) {
            int minHeight = std::min(heights[l], heights[r]);
            maxWater = std::max(maxWater, minHeight * (r-l));
            if (heights[l] < heights[r]) l++;
            else r--;
        }

        return maxWater;
    }
};
