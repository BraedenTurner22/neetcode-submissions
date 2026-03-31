import random

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def backtracking(arr, i):
            if i >= len(nums):
                res.append(arr.copy())
                return
            for x in range(i, len(arr)):
                arr[x], arr[i] = arr[i], arr[x]
                backtracking(arr, i+1)
                arr[x], arr[i] = arr[i], arr[x]
        
        backtracking(nums, 0)
        return res