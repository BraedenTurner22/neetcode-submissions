class Solution:

    def encode(self, strs: List[str]) -> str:
        concat = ""
        for string in strs:
            concat += str(len(string)) + "@" + string
        
        return concat

    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0

        while i < len(s):
            j = i
            currentNum = ""
            while s[j] != "@":
                currentNum += s[j]
                j += 1
            decodedStrings.append(s[j+1:j+int(currentNum)+1])
            i = j + int(currentNum) + 1
            currentNum = ""
        
        return decodedStrings