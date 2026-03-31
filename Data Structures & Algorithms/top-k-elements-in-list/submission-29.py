class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        numToFreq = defaultdict(int)
        mostFreq = [[] for i in range(len(nums)+1)]
        most = []

        for num in nums:
            numToFreq[num] += 1
        
        for num in numToFreq:
            count = numToFreq[num]
            mostFreq[count].append(num)

        for i in range(len(mostFreq)-1, 0, -1):
            for val in mostFreq[i]:
                most.append(val)
                if len(most) == k:
                    return most