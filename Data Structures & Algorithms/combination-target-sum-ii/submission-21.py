class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def dfs(arr, i, total):
            if total == target:
                res.append(arr.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            arr.append(candidates[i])
            dfs(arr, i+1, total + candidates[i])

            arr.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(arr, i+1, total)
        
        dfs([], 0, 0)

        return res