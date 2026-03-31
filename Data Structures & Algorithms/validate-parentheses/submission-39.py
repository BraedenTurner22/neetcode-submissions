class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenMap = {"{":"}", "(":")", "[":"]"}

        for paren in s:
            if paren in parenMap:
                stack.append(paren)
            elif stack and paren == parenMap[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return not stack