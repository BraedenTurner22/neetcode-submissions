class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        values = set(nums)

        for num in values:
            tempNum = num
            currLongest = 1
            while tempNum - 1 in values:
                currLongest += 1
                tempNum -= 1
            longest = max(longest, currLongest)
        
        return longest