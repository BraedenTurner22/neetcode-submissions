class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numToCount = {}
        indexToCount = [[] for i in range(len(nums)+1)]

        for num in nums:
            numToCount[num] = 1 + numToCount.get(num, 0)

        for num, index in numToCount.items():
            indexToCount[index].append(num)
        
        response = []

        for i in range(len(indexToCount)-1, 0, -1):
            for j in indexToCount[i]:
                response.append(j)
                if len(response) == k:
                    return response