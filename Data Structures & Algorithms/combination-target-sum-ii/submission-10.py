class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(idx, array):
            if sum(array) == target:
                res.append(array.copy())
                return
            
            if sum(array) > target:
                return
            
            if idx >= len(candidates):
                return

            array.append(candidates[idx])
            dfs(idx+1,array)
            array.pop()
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1
            
            dfs(idx+1,array)
        
        dfs(0,[])
        return res