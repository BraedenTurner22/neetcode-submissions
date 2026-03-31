class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded = encoded + str(len(string)) + "@" + string

        return encoded

    def decode(self, s: str) -> List[str]:
        decodedStrings = []

        i = 0
        while i < len(s):
            j = i
            wordLength = ""
            while s[j] != "@":
                wordLength = wordLength + s[j]
                j += 1
            decodedStrings.append(s[j+1:j+int(wordLength)+1])
            i = j + int(wordLength) + 1
            wordLength = ""
        return decodedStrings