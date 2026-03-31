class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        differenceDict = defaultdict()

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in differenceDict:
                return [differenceDict[diff], i]
            
            differenceDict.update({nums[i] : i})