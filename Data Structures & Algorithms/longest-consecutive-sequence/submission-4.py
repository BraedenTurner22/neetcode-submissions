class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        existingValues = set(nums)
        currentSequence = 1
        longestSequence = 1

        for num in existingValues:
            i = 1
            while num+i in existingValues:
                currentSequence += 1
                i += 1
            longestSequence = max(currentSequence, longestSequence)
            currentSequence = 1
        
        return longestSequence
