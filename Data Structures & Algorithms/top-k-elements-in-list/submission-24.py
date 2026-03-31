from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numToFreq = defaultdict(int)
        
        groupedNums = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numToFreq[num] += 1
        
        for num in numToFreq:
            groupedNums[numToFreq[num]].append(num)
        
        res = []
        for i in range(len(groupedNums)-1, 0, -1):
            for num in groupedNums[i]:
                res.append(num)
                if len(res) == k:
                    return res