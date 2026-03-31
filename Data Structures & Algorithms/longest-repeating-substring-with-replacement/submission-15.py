class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charToFreq = defaultdict(int)
        maxCharInWindow = 0
        longestSubstring = 0
        
        l = 0

        for r in range(len(s)):
            charToFreq[s[r]] += 1
            maxCharInWindow = max(maxCharInWindow, charToFreq[s[r]])
            while (r-l+1) - maxCharInWindow > k:
                charToFreq[s[l]] -= 1
                l += 1
            longestSubstring = max(longestSubstring, r-l+1) 
        
        return longestSubstring