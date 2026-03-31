class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numToIndexMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in numToIndexMap:
                return [numToIndexMap[diff], i]
            
            numToIndexMap.update({nums[i]: i})