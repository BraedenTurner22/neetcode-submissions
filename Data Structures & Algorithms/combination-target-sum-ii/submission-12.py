class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, array, total):
            if total == target:
                res.append(array.copy())
                return
            
            if total > target:
                return
            
            if idx >= len(candidates):
                return

            array.append(candidates[idx])
            dfs(idx+1,array, total + candidates[idx])
            array.pop()
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1
            
            dfs(idx+1,array, total)
        
        dfs(0,[], 0)
        return res