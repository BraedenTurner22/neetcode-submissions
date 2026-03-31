class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeroCount = 0
        product = 1
        response = []

        # get zero count and product without zeros
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                product *= num
        
        if zeroCount > 1:
            return [0] * len(nums)
        
        for num in nums:
            if zeroCount == 1 and num != 0:
                response.append(0)
            elif zeroCount == 1 and num == 0:
                response.append(product)
            else:
                response.append(product//num)
        
        return response