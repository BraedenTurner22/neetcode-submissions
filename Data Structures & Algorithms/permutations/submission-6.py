class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtracking(arr, i):
            if i >= len(arr):
                res.append(arr[:])
                return
            for j in range(i, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]
                backtracking(arr, i+1)
                arr[i], arr[j] = arr[j], arr[i]
        
        backtracking(nums, 0)
        return res