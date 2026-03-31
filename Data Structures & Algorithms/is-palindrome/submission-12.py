class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = [c.lower() for c in s if c.isalnum()]
        return filtered_s == filtered_s[::-1]