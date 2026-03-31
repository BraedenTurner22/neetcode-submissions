class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        response = [0] * len(temperatures)
        stack = [] #temp, idx

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                response[stackIdx] = idx - stackIdx
            stack.append((temp, idx))
        
        return response