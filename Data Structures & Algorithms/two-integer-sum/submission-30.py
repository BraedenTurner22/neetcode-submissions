class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexDict = defaultdict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indexDict:
                return [indexDict[diff], i]
            indexDict.update({nums[i]: i})