class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myNums = set(nums)

        if len(myNums) != len(nums):
            return True

        return False