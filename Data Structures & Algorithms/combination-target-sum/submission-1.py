class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        response = []

        def dfs(arr, i):
            if i >= len(nums):
                return
            if sum(arr) > target:
                return
            elif sum(arr) < target:
                arr.append(nums[i])
                dfs(arr, i)
                arr.pop()
                dfs(arr, i+1)
            else:
                response.append(arr.copy())
                return
        
        dfs([], 0)
        return response