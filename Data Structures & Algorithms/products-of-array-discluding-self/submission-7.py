class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prod, numZeros = 1, 0
        returnedList = []

        for num in nums:
            if num != 0:
                prod *= num
            else:
                numZeros += 1
            if numZeros > 1:
                return [0] * len(nums)
        
        for num in nums:
            if (numZeros == 1 and num == 0):
                returnedList.append(prod)
            elif (numZeros == 1 and num != 0):
                returnedList.append(0)
            else:
                returnedList.append(prod // num)
        
        return returnedList