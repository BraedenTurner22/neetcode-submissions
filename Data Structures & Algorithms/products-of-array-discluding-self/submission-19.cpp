class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int zeroCount = 0;
        int product = 1;
        vector<int> products;

        for (int& num : nums) {
            if (num == 0) zeroCount += 1;
            else product *= num;

            if (zeroCount > 1) {
                return std::vector<int>(nums.size(), 0);
            }
        }

        for (int& num : nums) {
            if (zeroCount == 1 && num != 0) products.push_back(0);
            else if (zeroCount == 1 && num == 0) products.push_back(product);
            else products.push_back(product / num);
        }

        return products;

    }
};
