class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChars = set()

        l = 0
        maxSequence = 0

        for r in range(len(s)):
            while s[r] in seenChars:
                seenChars.remove(s[l])
                l += 1
            seenChars.add(s[r])
            maxSequence = max(maxSequence, r - l + 1)
        
        return maxSequence