class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(ss, i):
            if i >= len(nums):
                res.append(ss.copy())
                return ss
            ss.append(nums[i])
            dfs(ss, i+1)
            ss.pop()
            dfs(ss, i+1)
        
        dfs([], 0)
        return res