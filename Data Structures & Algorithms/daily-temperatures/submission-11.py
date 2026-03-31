class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        output = [0] * len(temperatures)

        for r in range(len(temperatures)):
            while stack and temperatures[r] > temperatures[stack[-1]]:
                l = stack.pop()
                output[l] = r - l
            stack.append(r)
        
        return output