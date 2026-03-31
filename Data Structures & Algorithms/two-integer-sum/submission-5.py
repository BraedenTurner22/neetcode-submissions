class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsMap:
                return [numsMap[diff], i]
            numsMap.update({nums[i]: i})
