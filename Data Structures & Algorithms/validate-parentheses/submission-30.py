class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        parenMap = {"{":"}",
                    "[":"]",
                    "(":")"}
        
        stack = []

        for char in s:
            if char in parenMap:
                stack.append(parenMap[char])
            elif stack and stack[-1] == char:
                stack.pop()
            else:
                return False
        
        return not stack


