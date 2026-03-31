class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minHours = r

        while l <= r:
            k = (l+r) // 2
            totalHours = 0

            for p in piles:
                totalHours += math.ceil(float(p) / k)
            
            if totalHours <= h:
                minHours = k
                r = k - 1
            else:
                l = k + 1
        
        return minHours