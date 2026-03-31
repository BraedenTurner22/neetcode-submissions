class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNumsToIndex = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in seenNumsToIndex:
                return [seenNumsToIndex[diff], i]\
            
            seenNumsToIndex[nums[i]] = seenNumsToIndex.get(nums[i], i)
