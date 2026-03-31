class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        parenMaps = {'{':'}', '(':')', '[':']'}
        parenStack = []

        for paren in s:
            if paren in parenMaps:
                parenStack.append(parenMaps[paren])
            elif not parenStack or paren != parenStack[-1]:
                return False
            else:
                parenStack.pop()
        
        return not parenStack
