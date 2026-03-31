class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqDict = {}
        indexToOccurrence = [[] for i in range(len(nums)+1)]

        mostFrequentElements = []

        for num in nums:
            freqDict[num] = 1 + freqDict.get(num, 0)

        for n, o in freqDict.items():
            indexToOccurrence[o].append(n)
        
        for i in range(len(indexToOccurrence)-1, 0, -1):
            for num in indexToOccurrence[i]:
                mostFrequentElements.append(num)
                if len(mostFrequentElements) == k:
                    return mostFrequentElements
