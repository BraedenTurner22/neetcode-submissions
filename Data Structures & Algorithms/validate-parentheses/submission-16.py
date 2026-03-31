class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        parenMap = {"{" : "}", "(" : ")", "[" : "]",}
        stack = []

        for paren in s:
            if paren in parenMap:
                stack.append(parenMap[paren])
            elif stack and paren == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack