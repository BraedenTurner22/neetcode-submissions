class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lettersToWordsDict = defaultdict(list)

        for string in strs:
            charCount = [0] * 26
            for char in string:
                charCount[ord(char)-ord('a')] += 1
            lettersToWordsDict[tuple(charCount)].append(string)
        
        return list(lettersToWordsDict.values())