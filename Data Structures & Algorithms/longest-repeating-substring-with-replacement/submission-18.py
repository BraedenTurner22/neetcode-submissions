class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charToFreq = defaultdict(int)
        maxChar = 0

        res = 0

        l = 0

        for r in range(len(s)):
            charToFreq[s[r]] += 1
            maxChar = max(maxChar, charToFreq[s[r]])
            while r-l+1-maxChar > k:
                charToFreq[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res