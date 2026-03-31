class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #count num frequency
        numToFreq = defaultdict(int)
        freqIndexes = [[] for i in range(len(nums)+1)]
        biggestNums = []

        for num in nums:
            numToFreq[num] += 1
        
        for n, f in numToFreq.items():
            freqIndexes[f].append(n)
        
        for i in range(len(freqIndexes)-1, 0, -1):
            for num in freqIndexes[i]:
                biggestNums.append(num)
                if len(biggestNums) == k:
                    return biggestNums
        
