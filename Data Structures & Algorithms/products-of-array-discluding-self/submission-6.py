class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod, numZeros = 1, 0
        returnedList = []

        for num in nums:
            if num:
                prod *= num
            else:
                numZeros += 1
            
            if numZeros >= 2:
                return [0] * len(nums)
            
        for num in nums:
            if (numZeros == 1 and num != 0):
                returnedList.append(0)
            elif (numZeros == 1 and num == 0):
                returnedList.append(prod)
            else:
                returnedList.append(int(prod / num))
        
        return returnedList