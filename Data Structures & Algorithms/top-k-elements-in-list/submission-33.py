class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        charToFreq = defaultdict(int)
        numFrequency = [[] for i in range(len(nums)+1)]
        response = []


        for num in nums:
            charToFreq[num] += 1
        
        for c, f in charToFreq.items():
            numFrequency[f].append(c)
        
        for i in range(len(numFrequency)-1, 0, -1):
            for num in numFrequency[i]:
                response.append(num)
                if len(response) == k:
                    return response