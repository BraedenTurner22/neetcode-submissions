class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        tempDifferences = [0] * len(temperatures)

        for r in range(len(temperatures)):
            while stack and temperatures[r] > temperatures[stack[-1]]:
                l = stack.pop()
                tempDifferences[l] = r - l
            stack.append(r)
        
        return tempDifferences