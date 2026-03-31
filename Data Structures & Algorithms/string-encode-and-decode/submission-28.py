class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedString = ""

        for string in strs:
            encodedString += str(len(string)) + "#" + string

        return encodedString

    def decode(self, s: str) -> List[str]:

        decodedStrings = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            lenOfCurrentString = int(s[i:j])
            i = j + 1
            j = i + lenOfCurrentString
            newString = s[i:j]
            decodedStrings.append(newString)
            i = j
        
        return decodedStrings