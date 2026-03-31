from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charToFreq = defaultdict(int)

        l = 0
        response = 0

        maxSeenVal = 0
        for r in range(len(s)):
            charToFreq[s[r]] += 1
            maxSeenVal = max(maxSeenVal, charToFreq[s[r]])

            while (r - l + 1) - maxSeenVal > k:
                charToFreq[s[l]] -= 1
                l += 1
            response = max(response, r-l+1)
        
        return response