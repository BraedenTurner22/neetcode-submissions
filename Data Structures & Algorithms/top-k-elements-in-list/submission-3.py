class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        frequencyArrays = [[] for i in range(len(nums) + 1)]

        returnedList = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, cnt in count.items():
            frequencyArrays[cnt].append(num)
        
        for n in range(len(frequencyArrays)-1, 0, -1):
            for j in frequencyArrays[n]:
                returnedList.append(j)
                if len(returnedList) == k:
                    return returnedList