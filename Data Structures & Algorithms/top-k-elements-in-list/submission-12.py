class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numberFreq = {}
        indexFreqToNumber = [[] for i in range(len(nums)+1)]

        returnedList = []

        for num in nums:
            numberFreq[num] = 1 + numberFreq.get(num, 0)
        
        for num, count in numberFreq.items():
            indexFreqToNumber[count].append(num)
        
        for i in range(len(indexFreqToNumber)-1, 0, -1):
            for j in indexFreqToNumber[i]:
                returnedList.append(j)
                if len(returnedList) == k:
                    return returnedList