class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        charToFreq = defaultdict(int)
        maxFreq = 0

        longestSub = 0

        for r in range(len(s)):
            charToFreq[s[r]] += 1
            maxFreq = max(maxFreq, charToFreq[s[r]])
            while (r-l)+1 - maxFreq > k:
                charToFreq[s[l]] -= 1
                l += 1
            longestSub = max(longestSub, r-l+1)
        
        return longestSub