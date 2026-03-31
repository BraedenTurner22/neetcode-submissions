class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dups = set()

        for number in nums:
            if number in dups:
                return True
            dups.add(number)
        
        return False