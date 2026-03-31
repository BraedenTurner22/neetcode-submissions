class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        sLettersFreq = defaultdict()
        tLettersFreq = defaultdict()

        for i in range(len(s)):
            sLettersFreq[s[i]] = 1 + sLettersFreq.get(s[i], 0);
            tLettersFreq[t[i]] = 1 + tLettersFreq.get(t[i], 0);

        return sLettersFreq == tLettersFreq;