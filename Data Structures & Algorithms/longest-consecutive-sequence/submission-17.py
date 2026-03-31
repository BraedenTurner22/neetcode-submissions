class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seenValues = set(nums)
        longestSequence = 0

        for num in nums:
            if num - 1 not in seenValues:
                length = 1
                while num + length in nums:
                    length +=1
                longestSequence = max(longestSequence, length)
        
        return longestSequence