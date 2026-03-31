class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        response = []

        def dfs(arr, i, total):
            if i >= len(nums):
                return
            if total > target:
                return
            elif total < target:
                arr.append(nums[i])
                total += nums[i]
                dfs(arr, i, total)
                arr.pop()
                total -= nums[i]
                dfs(arr, i+1, total)
            else:
                response.append(arr.copy())
                return
        
        dfs([], 0, 0)
        return response