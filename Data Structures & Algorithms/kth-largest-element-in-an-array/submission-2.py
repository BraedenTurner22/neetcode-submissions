import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify(nums)

        diff = len(nums) - k

        while diff > 0:
            heapq.heappop(nums)
            diff -= 1
        
        return nums[0]