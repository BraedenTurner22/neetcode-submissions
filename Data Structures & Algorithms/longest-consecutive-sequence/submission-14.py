class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        seenNums = set(nums)
        longest = 0

        for num in nums:
            if num - 1 != seenNums:
                length = 1
                while num + length in nums:
                    length += 1
                longest = max(length, longest)
        
        return longest