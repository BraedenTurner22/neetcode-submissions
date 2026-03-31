class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsDict = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numsDict:
                return [numsDict[diff], i]
                
            numsDict.update({nums[i] : i})
