from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1) - 1

        s1Map = defaultdict(int)
        s2Map = defaultdict(int)

        for char in s1:
            s1Map[char] += 1

        # build initial window
        for i in range(len(s1)):
            s2Map[s2[i]] += 1

        while r < len(s2):
            if s2Map == s1Map:
                return True

            s2Map[s2[l]] -= 1
            if s2Map[s2[l]] == 0:
                del s2Map[s2[l]]
            l += 1

            r += 1
            if r < len(s2):
                s2Map[s2[r]] += 1

        return False
