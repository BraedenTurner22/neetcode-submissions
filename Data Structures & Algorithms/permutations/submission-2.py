import random

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def backtracking(arr, i):
            if i >= len(arr):
                res.append(arr.copy())
                return
            for j in range(i, len(arr)):
                arr[j], arr[i] = arr[i], arr[j]
                backtracking(arr, i+1)
                arr[j], arr[i] = arr[i], arr[j]
        
        backtracking(nums, 0)
        return res