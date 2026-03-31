class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        allWater = 0
        
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                maxLeft = max(maxLeft, height[l])
                allWater += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                allWater += maxRight - height[r]
        
        return allWater