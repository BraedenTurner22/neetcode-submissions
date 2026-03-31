class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seenVals = set()

        for number in nums:
            if number in seenVals:
                return True
            seenVals.add(number)
        
        return False