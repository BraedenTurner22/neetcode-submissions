class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        charToFreq = defaultdict(int)
        maxSeenCharCount = 0

        longestSubstring = 0


        l = 0
        for r in range(len(s)):
            charToFreq[s[r]] += 1
            maxSeenCharCount = max(maxSeenCharCount, charToFreq[s[r]])
            while (r-l)+1 - maxSeenCharCount > k:
                charToFreq[s[l]] -= 1
                l += 1
            longestSubstring = r-l+1
        
        return longestSubstring