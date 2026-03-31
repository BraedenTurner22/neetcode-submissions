class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversedString = ""

        for c in s:
            if c.isalnum():
                reversedString += c.lower()
        
        return reversedString == reversedString[::-1]