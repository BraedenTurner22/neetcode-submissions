class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> numToFreq = {};
        vector<vector<int>> indexToNumFreq(nums.size()+1);
        vector<int> result;

        for (int& num : nums) {
            numToFreq[num]++;
        }

        for (const auto& [num, freq] : numToFreq) {
            indexToNumFreq[freq].push_back(num);
        }

        for (int i = indexToNumFreq.size()-1; i > 0; i--) {
            for (int n : indexToNumFreq[i]) {
                result.push_back(n);
                if (result.size() == k) return result;
            }
        }

        return result;
    }
};
