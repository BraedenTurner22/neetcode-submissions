class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     encodedString = ""

    #     for string in strs:
    #         encodedString += str(len(string)) + "#" + string
    
    #     return encodedString


    # def decode(self, s: str) -> List[str]:

    #     decodedStringList = []
    #     i = 0

    #     while i < len(s):
    #         j = i
    #         while s[j] != '#':
    #             j += 1
    #         stringLength = int(s[i:j])
    #         i = j + 1
    #         j = i + stringLength

    #         newString = s[i:j]
    #         decodedStringList.append(newString)
    #         i == j
        
    #     return decodedStringList

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res