from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or s == "":
            return ""
        
        tMap = {}
        for c in t:
            tMap[c] = 1 +tMap.get(c, 0)
        
        res = [-1, -1]
        resLength = float("inf")

        have = 0
        need = len(tMap)

        haveMap = {}

        l = 0
        for r in range(len(s)):
            c = s[r]
            haveMap[c] = 1 + haveMap.get(c, 0)

            if c in tMap and haveMap[c] == tMap[c]:
                have += 1            

            while have == need:
                if r-l+1 < resLength:
                    resLength = r-l+1
                    res = [l, r]

                haveMap[s[l]] -= 1
                if s[l] in tMap and haveMap[s[l]] < tMap[s[l]]:
                    have -= 1

                l += 1
        l, r = res
        
        if resLength == float("inf"):
            return ""
        else:
            return s[l:r+1]
                 