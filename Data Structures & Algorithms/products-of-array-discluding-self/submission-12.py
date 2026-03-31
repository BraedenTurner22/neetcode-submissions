class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product = 1
        numZeros = 0

        returnedList = []

        for num in nums:
            if num == 0:
                numZeros += 1
                if numZeros > 1:
                    return [0] * len(nums)
            else:
                product = product * num
        
        for num in nums:
            if num != 0 and numZeros == 1:
                returnedList.append(0)
            elif num != 0 and numZeros == 0:
                returnedList.append(int(product/num))
            else:
                returnedList.append(product)
        
        return returnedList