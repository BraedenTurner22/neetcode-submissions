class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeroCount = 0
        totalProduct = 1

        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                totalProduct *= num

        if zeroCount >= 2:
            return [0] * len(nums)
        
        res = []

        for num in nums:
            if zeroCount == 1:
                if num == 0:
                    res.append(totalProduct)
                else:
                    res.append(0)
            else:
                res.append(totalProduct//num)

        return res