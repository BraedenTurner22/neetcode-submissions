class Solution:
    def findMin(self, nums: List[int]) -> int:

        response = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                response = min(response, nums[l])
                break
            
            m = (l + r) // 2
            response = min(response, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        




        return response
