class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        seenChar = set()

        l, r = 0, 1
        longest = 0

        while r < len(s):
            seenChar.add(s[l])
            while s[r] in seenChar:
                seenChar.remove(s[l])
                l += 1
            seenChar.add(s[r])
            r += 1
            longest = max(longest, r-l)
        
        return longest
