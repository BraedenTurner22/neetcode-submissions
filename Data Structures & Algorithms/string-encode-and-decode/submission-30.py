class Solution:

    def encode(self, strs: List[str]) -> str:
        combinedString = ''

        for word in strs:
            combinedString = combinedString + str(len(word)) + '@' + word
        
        return combinedString

    def decode(self, s: str) -> List[str]:
        listOfWords = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '@':
                j+= 1
            lenOfCurrentString = int(s[i:j])
            i = j + 1
            j = i + lenOfCurrentString
            newString = s[i:j]
            listOfWords.append(newString)
            i = j
        
        return listOfWords