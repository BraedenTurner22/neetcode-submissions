class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for l in range(n):
            if l > 0 and nums[l] == nums[l-1]:
                continue  # skip duplicate "first" values

            m, r = l + 1, n - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if total < 0:
                    m += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[m], nums[r]])
                    m += 1
                    r -= 1
                    # skip duplicates
                    while m < r and nums[m] == nums[m-1]:
                        m += 1
                    while m < r and nums[r] == nums[r+1]:
                        r -= 1

        return res
