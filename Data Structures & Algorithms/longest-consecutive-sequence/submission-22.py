class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        seen = set()

        for num in nums:
            seen.add(num)
        
        longestSequence = 1

        for num in nums:
            currentSequence = 1
            prev = num - 1
            while prev in seen:
                currentSequence += 1
                prev -= 1
            longestSequence = max(longestSequence, currentSequence)
        
        return longestSequence
