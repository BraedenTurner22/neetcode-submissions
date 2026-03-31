class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seenNums = defaultdict()

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seenNums:
                return [seenNums[diff], i]
            
            seenNums.update({nums[i]: i})