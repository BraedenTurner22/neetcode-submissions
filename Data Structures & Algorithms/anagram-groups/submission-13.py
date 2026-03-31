class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        charToWordDict = defaultdict(list)

        for string in strs:
            charCount = [0] * 26
            for char in string:
                charCount[ord(char)-ord('a')] += 1
            charToWordDict[tuple(charCount)].append(string)
        
        return charToWordDict.values()